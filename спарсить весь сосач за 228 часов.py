from bs4 import BeautifulSoup
import requests
import random
from telethon import TelegramClient, errors
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import datetime
import re, time
from array import *

# программа парсинга всего текста со всех разделов сосача
# который потом можно собрать с помощью цепей маркова

response = requests.get('https://2ch.hk/b/catalog.json').json()

length = len(response['threads'])

threads = response['threads']

symbols = ['?', '!', '.', ',', ':', '(', ')', '-', '=', '+', '/', '*']
nahuy_symbols = ['"', '<', '«', '»']


class MarkovChain:

    def __init__(self):
        self.worddict = {}

    def add_text(self, text):
        text = text.lower()
        words = text.split()
        for x in range(len(words) - 1):
            word = words[x]
            next_word = words[x + 1]

            if word not in self.worddict:
                self.worddict[word] = {}
            if next_word not in self.worddict[word]:
                self.worddict[word][next_word] = 1
            else:
                self.worddict[word][next_word] += 1

    def _get_word(self, word):
        if not word in self.worddict:
            return False

        n_words = []
        for n_word in self.worddict[word]:
            for x in range(self.worddict[word][n_word]):
                n_words.append(n_word)

        return random.choice(n_words)

    def generate_text(self, length):
        word = random.choice(list(self.worddict.keys()))

        while word in symbols:  # первое слово не может быть спецсимволом
            word = random.choice(list(self.worddict.keys()))

        text = word[0].upper() + word[1:]  # первое слово с большой буквы

        for x in range(length):
            o_word = word
            word = self._get_word(o_word)

            if not word:  # если для данного слова нет следующих за ним
                word = random.choice(list(self.worddict.keys()))
                while word in symbols:  # первое слово не может быть спецсимволом
                    word = random.choice(list(self.worddict.keys()))
                if o_word not in symbols:  # если предыдущее слово - не спецсимвол, то начинаем новое предложение
                    text += '.'
                    word = word[0].upper() + word[1:]  # первое слово с большой буквы
                text += ' ' + word

            else:  # если всё ок
                if word not in symbols:
                    if o_word in ['.', '!', '?']:  # если предыдущее слово - символ конца предложения
                        word = word[0].upper() + word[1:]  # первое слово с большой буквы
                    text += ' ' + word
                else:
                    text += word
            word = word.lower()

        return text


markov = MarkovChain()
boards = ['b', 'vg', 'po', 'fag', 'news', 'mobi', '2d', 'biz', 'hw', 'sex', 'v', 'wm', 'a', 'by', 'kpop', 'mov', 'au', 'rf', 'fa', 'alco', 'wrk', 'ma', 'cg', 'w', 'hry', 'pr', 'p', 'psy', 'tes', 'mu', 'soc', 'fiz', 'ftb', 's', 'tv', 'fs', 'es', 'un', 'gg', 'me', 'bo', 'em', 'fd', 'gd', 'spc', 'gsg', 'sp', 'fg', 'hc', 'gabe', 'dr', 'math', 'mus', 'mo', 'vn', 'sci', 'pa', 'td', 'fur', 'fet', 'wr', 'zog', 'mmo', 'bi', 'hi', 'mg', 'sn', 'dom', 'mc', 'ja', 'e', 'ra', 're', 'di', 'h', 'wow', 'ukr', 'ch', 'whn', 'fl', 'ga', 'obr', 'izd', 'law', 'brg', 'socionics', 'c', 'ne', 't', 'tr', 'diy', 'asmr', 'ho', 'br', 'cc', 'wp', 'bg', 'se', 'vape', 'ld', 'hh', 'mlp', 'sf', 'wh', 'rm', 'to', 'web', 'out', 'old', 'm', 'qtr4', 'smo', 'o', 'pok', 'wwe', 'ruvn', 'ew', 'pvc', 'ph', 'de', 'aa', 'r', 'trv', 'gb', 'moba', 'abu', 'cul', 'media', 'guro', 'ussr', 'jsf', 'sw', 'ya', 'r34', 'cute', 'kz', '8', 'mlpr', 'ro', 'who', 'srv', 'electrach', 'ing', 'got', 'crypt', 'lap', 'hg', 'sad', 'fi', 'nvr', 'ind', 'fem', 'vr', 'arg', 'char', 'hv', 'int', 'asylum', 'rf']

x = []

start = 0
stop = 0

full_start = time.time()

for i in range(1):
    response = requests.get(f'https://2ch.hk/b/catalog.json',
                            cookies={'usercode_auth': 'fb5d35839dc9eaf147debcbce5957bbc'}).json()
    threads = response['threads']
    for thread in threads:

        number = thread['num']

        r = requests.get(f'https://2ch.hk/b/res/{number}.json',
                         cookies={'usercode_auth': 'fb5d35839dc9eaf147debcbce5957bbc'})
        if r.status_code != 200:
            continue
        response_thread = r.json()
        post_list = response_thread['threads'][0]['posts']
        x.append(len(post_list))
        for post_dict in post_list:
            text = post_dict['comment']
            soup = BeautifulSoup(text, 'lxml')
            post_text = '\n'.join(soup.stripped_strings)
            if post_text != '':
                numbers = re.findall(r'>>\d+', post_text)  # список номеров
                for number in numbers:
                    post_text = post_text.replace(number, '')

                links = re.findall(r'http\S*', post_text)  # список с ссылками
                for link in links:
                    post_text = post_text.replace(link, '')

                for symbol in symbols:
                    post_text = post_text.replace(symbol, f' {symbol} ')
                    
                for symbol in nahuy_symbols:
                    post_text = post_text.replace(symbol, '')
                    
            markov.add_text(post_text)

full_stop = time.time()

print(markov.generate_text(100))

print('Тред', stop-start)
print('Всё время', full_stop-full_start)
            
print(min(x), max(x), sum(x))


