#!/usr/bin/env python

from configparser import ConfigParser
import bot_constants
import os
import logging


class BotfriendData:
    """
    This is Botfriend's knowledge store.
    Constants and static method data related to
    responding or processing go here. Provides data for the API calls

    """
    def __init__(self):

        # Clean this up

        c = ConfigParser()
        bc = bot_constants.BotConstants()
        self.config = c.read('botfriend.conf')
        self.config_file = 'botfriend.conf'
        self.greeting_keywords = bc.GREETING_KEYWORDS
        self.greeting_responses = bc.GREETING_RESPONSES
        self.monikers = bc.MONIKERS
        self.saved_user_data = c.read('savedUserData.conf')
        self.saved_user_data_file = 'savedUserData.conf'

    def writeConfig(self):
        if os.path.isfile(self.config_file):
            os.rename(self.config_file, self.config_file+ ".bak")
            logging.info("Writing to ConfigFile with new data")
            with open(self.config_file, 'w') as configFile:
                self.config.write(configFile)


class Botfriend:

    # Main botfriend class

    def __init__(self, BotfriendData):

        self.BotfriendData = BotfriendData
