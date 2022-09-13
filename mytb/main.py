import telebot
from telebot import types
import mytb as tb

bot = telebot.TeleBot('5628150286:AAF2Ok2uLCXCChDSaDLzrBEgE3NFLc2DlJQ')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f'<b>Здравствуй, {message.from_user.first_name}!</b>',
                     parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton(f'{tb.office_building} Посетить сайт')
    price = types.KeyboardButton(f'{tb.bookmark_tabs} Скачать прайс')
    call = types.KeyboardButton(f'{tb.telephone} Позвонить')
    mail = types.KeyboardButton(f'{tb.e_mail} Написать')
    markup.add(website, price, call, mail)
    bot.send_message(message.chat.id, 'Возможности бота к твоим услугам:',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if tb.text_variants(message.text) == 'id':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}',
                         parse_mode='html')
    elif tb.text_variants(message.text) in tb.usertext_photo:
        photo = open('files/example.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,
                         f'Это пример изображения. На фото - разработчик \
                         этого бота {tb.smiling_face_with_smiling_eyes}. \
                         В этом блоке может быть комментарий к изображению.',
                         parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Не понял...', parse_mode='html')


bot.polling(non_stop=True)
