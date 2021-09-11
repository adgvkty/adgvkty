from bs4 import BeautifulSoup
import requests
import random
from telethon import TelegramClient, errors
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import re
import telebot
from telebot import types

bot = telebot.TeleBot('')

txts = ['жр.txt', 'мр.txt']

digits_pattern = re.compile(r'^[1-9]+', re.MULTILINE)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Если не дошло - пиши @adgvkty')

@bot.message_handler(commands=['xui'])
def xui_message(message):
    xui = gen_osk(5)
    bot.send_message(message.chat.id, f'{xui}')
    xui = ''

@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    print(query.query)
    length = query.query
    print(type(length))
    print(length)
    length = int(length)
    try:
        xui = gen_osk(length)
        result = types.InlineQueryResultArticle(
                id='1', title="Оскорбление",
                description=f"матюк: {xui}",
                input_message_content = types.InputTextMessageContent(
                message_text=f"{xui}"))
        bot.answer_inline_query(query.id, result, cache_time=2147483646)
    except Exception as e:
        print(f"{type(e)}\n{str(e)}")

def gen_osk(length):

    string = ''
    for l in range(length):
        string += ' ' + str(p_choice())
    string += ' ' + str(s_choice())
    string = string[1:]
    return string.capitalize()

def p_choice():
    p = open('прилагательные.txt', 'rb')
    p_words = p.read().splitlines()
    p_word = random.choice(p_words)
    return p_word.decode()


def s_choice():
    s = open(f'мр.txt', 'rb')
    s_words = s.read().splitlines()
    s_word = random.choice(s_words)
    return s_word.decode()


bot.polling()














