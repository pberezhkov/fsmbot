# -*- coding utf-8 -*-

import config
import telebot
from crawlers.sofascore import SofaScoreCrawler

if __name__ == '__main__':
    bot = telebot.TeleBot(config.token)

    @bot.message_handler(content_types=['text'])
    def handle_message(message):
        if message.text == '/tournaments':
            bot.send_message(message.chat.id, 'Loading tournaments...')
            crawler = SofaScoreCrawler('https://www.sofascore.com/')
            tournaments = crawler.get_tournaments()
            for trnmnt in tournaments:
                bot.send_message(message.chat.id, trnmnt)

    bot.polling(none_stop=True)
