from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import apiai, json

updater = Updater(token='  н е  с к а ж у  ')
dispatcher = updater.dispatcher



import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def textMessage(bot, update):
    request = apiai.ApiAI('9c773547d5db4dcf86bd8c4e9a921e2f').text_request()
    request.lang = 'ru'
    request.session_id = 'hlebchanbot'
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')

def start(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text="Йа - бот, говори со мною!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def somebody(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text="Хуямбади")

somebody_handler = CommandHandler('somebody', somebody)
dispatcher.add_handler(somebody_handler)

def oleg(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text="ПИДОРАС")

oleg_handler = CommandHandler('oleg', oleg)
dispatcher.add_handler(oleg_handler)

def slavaukraini(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text="САЛО УРОНИЛИ!!!!")

slavaukraini_handler = CommandHandler('slava_ukraini', slavaukraini)
dispatcher.add_handler(slavaukraini_handler)

def kasuali(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text="СМЕРТЬ КАЗУАЛАМ!1!!!")

kasuali_handler = CommandHandler('kasuali', kasuali)
dispatcher.add_handler(kasuali_handler)

def chatid(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text=chat_id)

chatid_handler = CommandHandler('chat_id', chatid)
dispatcher.add_handler(chatid_handler)


def danek(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text="balabol")

danek_handler = CommandHandler('danek', danek)
dispatcher.add_handler(danek_handler)

def kpnl(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text="Слава КНПЛ!")

kpnl_handler = CommandHandler('kpnl',kpnl)
dispatcher.add_handler(kpnl_handler)

def dkr(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text="А вот не надо угрожать, ты че, я ж ниче, а оно вон чё")


dkr_handler = CommandHandler('dkr',dkr)
dispatcher.add_handler(dkr_handler)

def fiziki(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text="ДОЛБОЕБЫ!")

fiziki_handler = CommandHandler('fiziki',fiziki)
dispatcher.add_handler(fiziki_handler)

def piter(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text="Ыхыхы, смешная рифма могла бы быть))0)")

piter_handler = CommandHandler('piter',piter)
dispatcher.add_handler(piter_handler)

def himiki(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text="ДЕГЕНЕРАТЫ!")

himiki_handler = CommandHandler('himiki',himiki)
dispatcher.add_handler(himiki_handler)

def zavtravshk(bot, update):
                    bot.send_message(chat_id=update.message.chat_id, text="Ну бляяяяяяяяяяяяяяяяяяяяя")

zavtravshk_handler = CommandHandler('zavtra_v_shk',zavtravshk)
dispatcher.add_handler(zavtravshk_handler)

text_message_handler = MessageHandler(Filters.text, textMessage)
dispatcher.add_handler(text_message_handler)

updater.start_polling()
