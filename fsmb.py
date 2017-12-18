# -*- coding utf-8 -*-

import config
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    if message.text == 'и' or message.text == 'И':
        bot.send_message(chat_id=message.chat.id, text='горь')
    else:
        bot.send_message(chat_id=message.chat.id, text='чивооо блядь')


if __name__ == '__main__':
    bot.polling(none_stop=True)
