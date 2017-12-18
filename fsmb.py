# -*- coding utf-8 -*-

import config
import telebot

if __name__ == '__main__':
    bot = telebot.TeleBot(config.token)

    @bot.message_handler(content_types=['text'])
    def handle_message(message):
        pass  # todo

    bot.polling(none_stop=True)
