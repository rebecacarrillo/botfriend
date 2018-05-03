#!/usr/bin/env python

import logging
import bot_constants
from configparser import ConfigParser
import botfriend_helpers
import botfriend_api
from fire import Fire

# Initialize the bot and prompt for input
def begin_bot(name=False):

    bfd = botfriend_api.BotfriendData()
    bf = botfriend_api.Botfriend(bfd)
    bh = botfriend_helpers.BotfriendHelpers()

    Config = ConfigParser()

    if(name):
        dont_introduce()
    else:
        name = input("Hey! My name is DBot. What's your name? \n>>> ")
        print("Cool. Hi " + name)
        factoids = input("Anything special you want me to know about you? \n>>> ")
        print("Intriguing. I'll keep that in mind.") #create a constants dict for this so it's not the same everytime.

        saved_user_data = open(bfd.saved_user_data_file, 'w')
        Config.add_section('User')
        Config.set('User', 'Name', name)
        Config.set('User', 'Factoids', factoids)
        Config.write(saved_user_data)
        saved_user_data.close()


def dont_introduce():
    pass



def main():
    Fire(begin_bot)


if __name__ == '__main__':
    main()