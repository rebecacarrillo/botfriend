#!/usr/bin/env python

from configparser import ConfigParser
import os
from time import sleep
import json
import logging
import re
import aiml
import ws4py
from textblob import TextBlob
import bot_constants
import random
from ws4py.client.threadedclient import WebSocketClient


class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False


class BotfriendData:
    """
    This is Botfriend's knowledge store.
    Constants and static method data related to
    responding or processing go here. Provides data for the API calls

    """
    def __init__(self):

        c = ConfigParser()
        self.config = c.read('botfriend.conf')
        self.config_file = 'botfriend.conf'
        self.greeting_keywords = bot_constants.GREETING_KEYWORDS
        self.greeting_responses = bot_constants.GREETING_RESPONSES
        self.dTimeout = self.config.getfloat("general","disconnect_timeout")
        self.wsTimeout = self.config.get("general", )
        self.monikers = bot_constants.MONIKERS
        self.myName = self.config.get("general", "my_name")


    def writeConfig(self):
        if os.path.isfile(self.config_file)
            os.rename(self.config_file, self.config_file+ ".bak")
            logger.info("Writing to ConfigFile with new data")
            with open.(self.config_file, 'w') as configFile:
                self.config.write(configFile)


    def newMessage(self, **kwargs):
        msg = {}
        method = kwargs.pop("method")
        for methodName in switch(method):
            if methodName('clientConnect'):
                msg = {
                    'txnID': self.txnIDs["clientConnectTxnID"],
                    'method': 'clientConnect',
                }
                break
            if methodName('clientDelivered'):
                senderGuid = kwargs.pop("senderGuid")
                threadID = kwargs.pop("threadID")
                messageID = kwargs.pop("messageID")
                msg = {'method': 'clientDelivered'
                       , 'txnId': str(uuid4)
                       , 'messageID': messageID
                       , 'threadID': threadID
                       , 'senderGuid': senderGuid
                       }
                break
            if methodName("clientThreadMessageTxt"):
                threadID = kwargs.pop("threadID")
                responseText = kwargs.pop("responseText")
                msg = {'txnID': str(uuid4())
                    , 'method': 'clientThreadMessage'
                    , 'threadID': threadID
                    , 'msgID': str(uuid4())
                    , 'contentType': 'text'
                    , 'data': responseText
                       }
                break
        return msg


class Botfriend:

    """ Main Botfriend class
    """
    def __init__(self, BotfriendData):

        self.BotfriendData = BotfriendData
        self.myName = BotfriendData.myName
        self.threadID =''
        self.threadCreateTxnID = ''
        self.resultString = ''
        self.greeting_keywords = self.knowledge.greeting_keywords
        self.greeting_responses = self.knowledge.greeting_responses
        self.welcomeString = " Hi, I'm {}. Let's talk".format(self.myName)

    # -------------------------------------------- #
    # ---------- WEBSOCKET STUFF ----------------- #
    #--------------------------------------------- #

    def startWS(self):
        self.webSocket = WSClient(
            self,
            self.BotfriendData,
            heartbeat_freq=self.BotfriendData)

        self.webSocket.setup()

    def runMe(self):
        """
        Start the websocket client.
        """
        firstAppError = True

        while True:
            if (not self.terminate) and (not self.appError) and (not self.connected):
                self.startWS()
            elif (not self.terminate) and (self.appError):
                if firstAppError:
                    logging.info("Server disconnected")
                    firstAppError = False
                else:
                    logger.info("Sleeping...")

                sleep(BotfriendData.dTimeout)
                self.startWS()
            elif self.terminate:
                logging.info('Botfriend is terminating')
                self.webSocket.close()
                self.connected = False
                break
            else:
                logging.info('trying to reconnect')
                sleep(BotfriendData.dTimeout)
                pass

    def timeOut(self):
        """
        handles socket idling and timeout
        :return:
        """
        if self.idle_time > self.BotfriendData.wsTimeout:

            if self.connected:
                self.webSocket.close()
                self.webSocket.setup()
                self.idle_time = 0
            else:
                self.idle_time = 0
        else:
            self.idle_time += 1

    # TODO: define sendAck method


    def processMessage(self, textblob):

        self.idle_time = 0
        incMethod = blob['method']
        txnID = blob['txnID']

        #if (incMethod != 'ack'):
        #    self.sendAck(txnID)

        #for incomingMethod in switch(incMethod):
        #    if incomingMethod('ack'):
        #        txnID = blob['txnID']
        #        if txnID == self.BotfriendData.txnIDs['clientConnectTxnID'] :
        #            self.currentStatus = 'clientConnectAcked'

        if incomingMethod('serverThreadMessage'):
            threadID = blob['threadID']
            threadIDStr = blob['threadID']
            messageType = blob.get('contentType', 'text')
            should_respond = False
            should_respond = ResponsePermission.ResponsePermission.shouldRespondToThread(threadID)
            if should_respond:
                senderGuid = blob['senderGuid']
                msgID = blob['msgID']
                method = {"method": "clientDelivered"
                    , "threadID": threadID
                    , "messageID": messageID
                    , "senderGuid": senderGuid}
                self.sendResponse(**method)
                method = {"method": "clientRead"
                    , "threadID": threadID
                    , "messageID": messageID
                    , "senderGuid": senderGuid}
                self.sendResponse(**method)

                if messageType == 'text':
                    data = blob.get('data', 'Hello, world,')
                    data_str = data
                    data_str = re.sub(r'[^\x00-\x7F]+', ' ', data_str)
                    if data_str[:3] == "end":
                        data_str = "Hello, World,"
                    try:
                        response_text = self.kernel.respond(data_str, threadIDStr)
                    except:
                        response_text = "Hmm..I don't know what to say"

                    if len(response_text) > 80 or len(response_text) == 0:
                        try:
                                data_str = "xfind it"
                                response_text = self.kernel.respond(data_str, threadIDStr)
                        except:
                                response_text = "Hmm..I don't know how to answer"

                    method = {"method": "clientThreadMessageTxt"
                        , "threadID": threadID
                        , "responseText": response_text}
                    self.sendResponse(**method)

            break



    class WSClient(WebSocketClient):
        def __init__(self, botfriend, botfriendData, *args, **kwargs):

            self.botfriend = botfriend
            self.botfriendData = BotfriendData
            self.args = args
            self.kwargs = kwargs
            self.url = self.botfriendData.serverURL

            WebSocketClient.__init__(self, self.url, *args, **kwargs)


        def setup(self, timeout=1):
                try:
                    self.connect()
                    signal.signal(signal.SIGALRM, self.handler)
                    self.botfriend.appError = False
                    self.botfriend.terminate = False
                    self.botfriend.connected = True
                    self.run_forever()
                except KeyboardInterrupt:
                    self.botfriend.terminate = True
                    self.close()
                    self.botfriend.connected = False
                except:
                    self.botfriend.appError = True
                    if self.sock is not None:
                        self.close()
                    self.botfriend.connected = False

        def opened(self):
            logging.info("Connected to Server")
            method = {"method": "clientConnect"}
            message = self.botfriendData.newMessage(**method)
            self.sendMessage(message)
            self.botfriend.ws_connected = True
            self.botfriend.connected = True

        def closed(self, code, reason=None):
            logging.info('Closing websocket connection')
            self.botfriend.connected = False
            if not self.botfriend.terminate:
                self.botfriend.appError = True
            else:
                self.botfriend.appError = False



        def received_message(self, msg):
                    message = json.loads(msg.data.decode('utf8'))
                    self.botfriend.traceLog.info("<< %s" % message)
                    # print("<< {0}".format(message), file=sys.stderr)
                    self.botfriend.idle_timeout = 0
                    self.botfriend.processMessage(message)

        def sendMessage(self, msg):
            if 'method' in msg:
                if msg['method'] == 'clientThreadMessage':
                self.send(json.dumps(msg))



    if __name__ == '__main__':

        if args.reg:
            botfriend = Botfriend(botfriendData,True)
            botfriend.startWS()

        else:
            botfriend = Botfriend(botfriendData)
            botfriend.runMe()



