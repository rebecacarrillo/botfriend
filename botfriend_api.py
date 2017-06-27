from configparser import ConfigParser
import logging
# aiml on its own doesn't work in python 3.
# Check requirements for python-aiml work around
import aiml
import ws4py
import bot_constants
import random


class BotfriendData:
    """
    This is Botfriend's knowledge store.
    Constants and static method data related to
    responding or processing go here.

    """
    def __init__(self):
        c = ConfigParser()
        self.config = c.read('botfriend.conf')
        self.greeting_keywords = bot_constants.GREETING_KEYWORDS
        self.greeting_responses = bot_constants.GREETING_RESPONSES
        self.monikers = bot_constants.MONIKERS


class Botfriend:
    def __init__(self, BotfriendData):

        self.knowledge = BotfriendData
        self.greeting_keywords = self.knowledge.greeting_keywords
        self.greeting_responses = self.knowledge.greeting_responses

    def look_for_i(self, msg):
        # I on its own generally refers to the pronoun "I"
        cleaned_words = []
        words = msg.split(' ')
        for w in words:
            if w == 'i':
                w = 'I'
            if w == "i'm":
                w = "I'm"
            cleaned_words.append(w)
        return ' '.join(cleaned_words)

    # def process_input(msg):

    # def parse_input

    # def respond(msg):
        # i_msg = look_for_i(msg)
        # parsed_msg = #parse the cleaned sentence
        # greeted = check_for_greeting(parsed_msg)

    def check_for_greeting(msg):
        """
        TODO: run this only in the first few
        dozen exchanges within a thread.
        """
        for word in msg.words:
            if word.lower() in self.greeting_keywords:
                return random.choice(self.greeting_responses)


    # (simple) linguistic methods
    #def find_pronoun(msg):
