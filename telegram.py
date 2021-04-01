# import telebot
# import tokenbot
# bot=telebot.TeleBot(tokenbot.TOKEN)
# @bot.message_handler(content_types=['start','help'])
# def cat(message):
#     bot.send_message(message.chat.id,message.text)
#
# bot.polling(none_stop=True)


import telebot
import random
import tokenbot
from telebot import  types

number=0
bot = telebot.TeleBot(tokenbot.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Хомяк Хома)) Родился я 11 февраля 2019г")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('да')
    item3 = types.KeyboardButton('нет')
    item2 = types.KeyboardButton('привет')
    markup.add(item1, item2,item3)
    bot.send_message(message.chat.id, "Хочень немного милоты?", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        if message.chat.type=='private':
            from PIL import Image
            # if message.text=='да':
            #     bot.send_message(message.chat.id, 'Колосо 😊')
            #     photo = open('/home/shifr/Desktop/Xoma/IMG_20201018_151032.png', 'rb')
            #     bot.send_photo(message.chat.id, photo)

            if message.text == 'да':
                number=random.randint(0,7)
                bot.send_message(message.chat.id, 'Колосо 😊')
                if number==0:
                        photo = open('/home/shifr/Desktop/Xoma/IMG_20201018_151032.png', 'rb')
                        bot.send_photo(message.chat.id, photo)
                        bot.send_message(message.chat.id, 'Надеюсь такую ты еще не видел😇\nВо всяком случае у меня запасы имеются, хоть и не большие😌\nПишите сюда www.instagram.com/smilpok/ с просьбой устроить полноценный фотосет 😆 для меня')
                elif number==1:
                    photo = open('/home/shifr/Desktop/Xoma/IMG-20201022-WA0003.jpg', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id,'Мне идет?')
                elif number==2:
                    photo = open('/home/shifr/Desktop/Xoma/IMG-20201022-WA0005.jpg', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, 'Бррр... Колодно🥶')
                elif number==3:
                    photo = open('/home/shifr/Desktop/Xoma/IMG-20201022-WA0006.jpg', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, 'Однажды мне подарили гамак и я его съел😑 я же хомяк')
                elif number==4:
                    photo = open('/home/shifr/Desktop/Xoma/IMG-20201022-WA0012.jpg', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, 'Ну качество конечно не очень. поэтому пишите на данный профиль www.instagram.com/smilpok/ с просьбой сделать качественные фото☺️')
                elif number==5:
                    photo = open('/home/shifr/Desktop/Xoma/IMG-20201022-WA0017.jpg', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id,'Да да да я всегда ем😃\nЩелкай устерднее на клавишу "да"')
                elif number==6:
                    photo = open('/home/shifr/Desktop/Xoma/IMG-20201022-WA0025.jpg', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, 'хрум')
                else:
                    photo = open('/home/shifr/Desktop/Xoma/IMG-20201022-WA0028.jpg', 'rb')
                    bot.send_photo(message.chat.id, photo)
                    bot.send_message(message.chat.id, 'Дратути, я Вас не звал, котики')
            elif message.text=='привет':
                from PIL import Image
                picture = open('/home/shifr/Desktop/Xoma/sticker.webp', 'rb')
                bot.send_sticker(message.chat.id, picture)
                bot.send_message(message.chat.id, '{0.first_name}!Рад тебя видеть фыр...\nЯ {1.first_name}🙂\nНажми "ДА" что-бы увидеть, что я для тебя приготовил'.format(message.from_user,bot.get_me()))

            elif message.text=='нет':
                number = random.randint(0, 1)
                if number == 0:
                    bot.send_message(message.chat.id, '😮 Фыр Фыр Фыр.... Если что, возвращайся🥴 никогда не поздно нажать "ДА"')
                else:
                    bot.send_message(message.chat.id, 'Не буди во мне ЗВЕРЯ!!!😡')
            else:
                number=random.randint(0,2)
                if number==0:
                    bot.send_message(message.chat.id,'Я не понимать, что ты говоришь, я же хомячёк🥺''\n''Во всяком случае мы можем начать с начала☺️''\n''Предлогаю тебе нажать "ДА", что-бы я мог тебя порадовать)\nИ да) с РЕГИСТРОМ пока подкачали, поэтому все в нижнем регистре!!!')
                elif number==1:
                    picture = open('/home/shifr/Desktop/Xoma/sticker1.webp', 'rb')
                    bot.send_sticker(message.chat.id, picture)
                    bot.send_message(message.chat.id,'НЕПОНЯТНО\nСЛОЖНА, СЛОЖНА, ну сложна же')
                else:
                    picture = open('/home/shifr/Desktop/Xoma/sticker1.webp', 'rb')
                    bot.send_sticker(message.chat.id, picture)

    except Exception as e:
        print(repr(e))

    # bot.reply_to(message, message.text)
bot.polling(none_stop=True)

