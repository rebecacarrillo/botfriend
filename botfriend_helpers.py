import bot_constants
import random
from botfriend_api import BotfriendData

bd = BotfriendData()

class BotfriendHelpers:

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

    # def create_response(pronoun=false, noun, verb):
    #    response = []

    #    if pronoun:
    #        response.append(pronoun)


    def check_for_greeting(msg):
        """
        TODO: run this only in the first few
        dozen exchanges within a thread.
    """
        for word in msg.words:
            if word.lower() in bd.greeting_keywords:
                return random.choice(bd.greeting_repsponses)


            # (simple) linguistic methods
            # def find_pronoun(msg):