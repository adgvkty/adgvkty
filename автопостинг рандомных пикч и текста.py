from bs4 import BeautifulSoup
import requests
import random
from telethon import TelegramClient, errors
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import datetime
import re

# берет случайную картинку и текст с двача, и постит в тг

client = TelegramClient('', , '')

boards = ['b', 'vg', 'po', 'fag', 'news', 'mobi', '2d', 'biz', 'hw', 'sex', 'v', 'wm', 'a', 'by', 'kpop', 'mov', 'au', 'rf', 'fa', 'alco', 'wrk', 'ma', 'cg', 'w', 'hry', 'pr', 'p', 'psy', 'tes', 'mu', 'soc', 'fiz', 'ftb', 's', 'tv', 'fs', 'es', 'un', 'gg', 'me', 'bo', 'em', 'fd', 'gd', 'spc', 'gsg', 'sp', 'fg', 'hc', 'gabe', 'dr', 'math', 'mus', 'mo', 'vn', 'sci', 'pa', 'td', 'fur', 'fet', 'wr', 'zog', 'mmo', 'bi', 'hi', 'mg', 'sn', 'dom', 'mc', 'ja', 'e', 'ra', 're', 'di', 'h', 'wow', 'ukr', 'ch', 'whn', 'fl', 'ga', 'obr', 'izd', 'law', 'brg', 'socionics', 'c', 'ne', 't', 'tr', 'diy', 'asmr', 'ho', 'br', 'cc', 'wp', 'bg', 'se', 'vape', 'ld', 'hh', 'mlp', 'sf', 'wh', 'rm', 'to', 'web', 'out', 'old', 'm', 'qtr4', 'smo', 'o', 'pok', 'wwe', 'ruvn', 'ew', 'pvc', 'ph', 'de', 'aa', 'r', 'trv', 'gb', 'moba', 'abu', 'cul', 'media', 'guro', 'ussr', 'jsf', 'sw', 'ya', 'r34', 'cute', 'kz', '8', 'mlpr', 'ro', 'who', 'srv', 'electrach', 'ing', 'got', 'crypt', 'lap', 'hg', 'sad', 'fi', 'nvr', 'ind', 'fem', 'vr', 'arg', 'char', 'hv', 'int', 'asylum', 'rf']

forbidden = [r'бамп.*$', r'(.* |^)реф.*( |$)']
regex = '('+'|'.join(forbidden)+')'


def get_picture(board):
    catalog = requests.get(f'https://2ch.hk/{board}/catalog.json',
                           cookies={'usercode_auth': 'fb5d35839dc9eaf147debcbce5957bbc'}).json()

    thread_num = random.choice(catalog["threads"])["num"]
    thread = requests.get(f'https://2ch.hk/{board}/res/{thread_num}.json',
                          cookies={'usercode_auth': 'fb5d35839dc9eaf147debcbce5957bbc'}).json()

    post = random.choice(thread["threads"][0]["posts"])
    while not post["files"]:
        post = random.choice(thread["threads"][0]["posts"])

    file = random.choice(post["files"])
    if file["type"] not in [1, 2]:
        return get_picture(board)

    path = file["path"]
    pic = requests.get('https://2ch.hk'+path,
                       cookies={'usercode_auth': 'fb5d35839dc9eaf147debcbce5957bbc'})
    return pic.content, f'https://2ch.hk/{board}/res/{thread_num}.html#{post["num"]}'


def get_post(board):
    try:
        catalog = requests.get(f'https://2ch.hk/{board}/catalog.json',
                               cookies={'usercode_auth': 'fb5d35839dc9eaf147debcbce5957bbc'}).json()

        thread_num = random.choice(catalog["threads"])["num"]
        thread = requests.get(f'https://2ch.hk/{board}/res/{thread_num}.json',
                              cookies={'usercode_auth': 'fb5d35839dc9eaf147debcbce5957bbc'}).json()

        post = random.choice(thread["threads"][0]["posts"])
        while not post["comment"]:
            post = random.choice(thread["threads"][0]["posts"])

        soup = BeautifulSoup(post["comment"], 'lxml')

        post_text = '\n'.join(soup.stripped_strings)
        if re.fullmatch(regex, post_text.lower()):
            return get_post(board)
        else:
            return post_text, f'https://2ch.hk/{board}/res/{thread_num}.html#{post["num"]}'

    except Exception as e:
        print(f'https://2ch.hk/{board}/res/{thread_num}.html#{post["num"]}')
        print(e)
        return get_post(board)


async def send_post(channel):
    pic_board = random.choice(boards)
    file, pic_thread = get_picture(pic_board)
    post_board = random.choice(boards)
    msg, post_thread = get_post(post_board)
    txt = f'\n[тред с пикчей]({pic_thread})\n[тред с постом]({post_thread})'
    try:
        await client.send_message(channel, message=msg+txt, file=file)
    except errors.rpcerrorlist.MediaCaptionTooLongError:
        await send_post(channel)
    print(f'Sent post at {channel} %s' % datetime.datetime.now())


client.start()

scheduler = AsyncIOScheduler()
scheduler.add_job(send_post, 'cron', minute='0,10,20,30,40,50', args=('govno_sosach', ), max_instances=3)

scheduler.start()

asyncio.get_event_loop().run_forever()
