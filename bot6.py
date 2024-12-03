import telebot
from audit import autitoriy
bot = telebot.TeleBot(token='7338816774:AAHXpIKW3_vnQhNOqfJ3n4Ou-k6lR-ZT2zY')


@bot.message_handler(commands=['start'])
def start(messages):
    bot.send_message(messages.chat.id, 'Привіт, я бот, який підкаже тобі завідувачів аудиторій, напиши номер аудиторії')


@bot.message_handler(content_types=['text'])
def find_auditorium_manager(message):
    cabinet_number = message.text
    if cabinet_number in autitoriy:
        bot.reply_to(message, f"Кабінет {cabinet_number}: {autitoriy[cabinet_number]}")
    else:
        bot.reply_to(message, f"Інформація про кабінет {cabinet_number} відсутня.")


bot.infinity_polling()
