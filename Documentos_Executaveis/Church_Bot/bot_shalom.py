##################################################### Library ##################################################################################################################

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler) #Library for telegram
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import requests #Library for requests
import logging #logs
import configparser #config
import datetime #Library for date
import requests #Requests URLs
import io #Library for bytes
import base64 #Library for base64
import hashlib #Library for hash
import datetime #Library for datetime
import json #library for json
import unidecode #accents

##################################################### Configs ##################################################################################################################

#-------------------------------------------------------#
#Description: Access the configuration of project
#Paramater token: Token of Telegram
#Parameter url: Endpoint to get data from web service
#Parameter parse_mode: Mode to show information
#Parameter platraform: Number of plataform
#Parameter filename: File where the logs will be write
#Author: João Lucas Flauzino Cassiano (joao.lucas@romaconsulting.com.br)
#Createat: 2019-06-26
#--------------------------------------------------------#

config = configparser.ConfigParser() #ConfigParser
config.read('C://Users//joni_//Documentos_Executaveis//Church_Bot//Config//config.ini') # Accessing the config files
token = config['TOKEN']['token'] #Accessing the token of Telegram
file = config['SERVICE_LOGS']['file']

#-------------------------------------------------------#
#Description: Save the logs
#Parameter filename: File for write logs
#Author: João Lucas Flauzino Cassiano (joao.lucas@romaconsulting.com.br)
#Createat: 2019-06-26
#--------------------------------------------------------#

logging.basicConfig(filename= file + datetime.datetime.now().strftime("%y%m%d") + '.logs', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO) #Save logs
logger = logging.getLogger(__name__) #logs

##################################################### Telegram functions ######################################################################################################

#-------------------------------------------------------#
#Description: This function denies when an user tries to send a file
#Paramater bot: Bot that is active
#Parameter update: Updates sent by interactions
#Return: Response to the user
#Author: João Lucas Flauzino Cassiano 
#Createat: 2019-01-30
#--------------------------------------------------------#

def send_files(bot, update):

    res = 'Desculpe, ainda não trabalho com esse tipo de mensagem.'
    update.message.reply_text(res, parse_mode = 'MARKDOWN')

#-------------------------------------------------------#
#Description: This function send an answer for the user
#Paramater bot: Bot that is active
#Parameter update: Updates sent by interactions
#Return: Response to the user
#Author: João Lucas Flauzino Cassiano 
#Createat: 2019-01-30
#--------------------------------------------------------#

def send_answer(bot, update, user_data):

    msg = unidecode.unidecode(update.message.text.lower())

    if 'agenda' in msg:
         update.message.reply_text('Você tem compromisso as 17h no sábado.', parse_mode = 'MARKDOWN')
    if 'horarios' in msg:
         update.message.reply_text('Hoje as palavras são as 17h, 19h e 21h.', parse_mode = 'MARKDOWN')
    if 'ingressos' in msg:
         update.message.reply_text('Os ingressos estão esgotados.', parse_mode = 'MARKDOWN')

    else:

        if msg == 'informacoes' or msg == 'ola' or msg == 'boa noite' or msg == 'bom dia' or msg == 'boa tarde' or msg == '/start':  

            buttons = [['Agenda', 'Horários', 'Ingressos']]
            markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True, pass_user_data=True, resize_keyboard=True)
            res = 'Olá ' + update.message.from_user.username + '! Tudo bem? Por favor, escolha o que deseja saber.'
            update.message.reply_text(res, parse_mode = 'MARKDOWN', reply_markup = markup)

        else:

            update.message.reply_text('Caso desejar mais alguma coisa, é só dizer "informações"', parse_mode = 'MARKDOWN')




####################################################### Main #################################################################################################################

#-------------------------------------------------------#
#Description: This function allows you to initialize the bot
#Author: João Lucas Flauzino Cassiano 
#Createat: 2019-06-26
#--------------------------------------------------------#

def main():

    #Create the Updater and pass it your bot's token
    updater = Updater(token)
    #use_context = True

    #Get the dispatcher to register handlers
    dp = updater.dispatcher

    #handler for message
    msg_txt_handler = MessageHandler(Filters.text | Filters.command, send_answer, pass_user_data = True)

    #Hanfler for video, photo, document, voice and sticker
    msg_handler = MessageHandler(Filters.video | Filters.photo | Filters.document | Filters.voice | Filters.sticker , send_files)

    #Dispatcher
    dp.add_handler(msg_txt_handler)

    #Dispatcher
    dp.add_handler(msg_handler)

    #Start the Bot
    updater.start_polling()

    #Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    #SIGTERM or SIGABRT. This should be used most of the time, since
    #start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

#Start the program
if __name__ == '__main__':

    main()
