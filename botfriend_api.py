from configparser import ConfigParser
import logging
import python-aiml
import ws4py

import bot_constants

class BotfriendData:
    """ 
    This is Botfriend's knowledge store.
    Constants and static method data related to 
    responding or processing go here.

    """
    def __init__(self):
        c=ConfigParser()
        self.config = c.read('botfriend.conf')
        self.greeting_keywords = GREETING_KEYWORDS
        self.greeting_responses = GREETING_RESPONSES
        self.monikers = MONIKERS

        

class Botfriend(BotfriendData):

    def __init__(self):

        self.knowledge = BotfriendData
        self.greeting_keywords = self.knowledge.greeting_keywords
        self.greeting_responses = self.knowledge.greeting_responses

        def process_input(input):
        
        def parse_input
            
        def respond(sentence):

        def check_for_greeting(sentence):
            """ run this only in the first few dozen exchanges within a thread """
            for word in sentence.words:
                if word.lower() in self.greeting_keywords:
                    return random.choice(self.greeting_responses)



