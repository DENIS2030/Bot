#Acces token APIAI - 53553db77f44416ab04548a10467a8ab
#Bottoken - 1145644752:AAGd80b5sne880ilU5DA5GEnUTdLSxM6rEs
import telebot
import apiai ,json

bot = telebot.TeleBot("1145644752:AAGd80b5sne880ilU5DA5GEnUTdLSxM6rEs")

@bot.message_handler(commands=['start'])
def sendStartMessage(message):
    bot.send_message(message.chat.id,'hi')

@bot.message_handler(content_types=['text'])
def semd_some_message(message):
    request = apiai.ApiAI('53553db77f44416ab04548a10467a8ab').text_request()
    request.lang = 'ru'
    request.session_id = 'lexabad9jsukabot'
    request.query = message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=message.chat.id,text=response)
    else:
        bot.send_message(chat_id=message.chat.id,text="I can't understand")

bot.polling()