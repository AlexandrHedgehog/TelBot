import telebot
from telebot import types

bot = telebot.TeleBot()

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'<b>Привет!</b> Я бот-турист.' \
           f'В некоторых странах я уже побывал и готов поделиться с тобой всем что поможет тебе посетить их!) , ' \
           f'<b>{message.from_user.first_name}</b> выбери страну из списка ниже'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    # parse_mode='html'
    # message.chat.id- через сообщение мы обратились к чату и получили его id
    # mess - текст, который мы передаём.
    # html - формат с тегами, с которыми м можем отправлять текст. например - <b> </b>
    # {message.from_user.first_name} - метод получение имени пользователя.
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    # Создаем переменную с указанием типа - подстрочная кнопка
    # (и указанием параметров - подстроения под экран, и колл-во кнопок в ряду)
    cuba = types.KeyboardButton('Куба')
    georgia = types.KeyboardButton('Грузия')
    bali = types.KeyboardButton('Бали')
    morocco = types.KeyboardButton('Марокко')
    taiwan = types.KeyboardButton('Тайвань')
    seychelles = types.KeyboardButton('Сейшелы')
    portugal = types.KeyboardButton('Португалия')
    norway = types.KeyboardButton('Норвегия')
    greece = types.KeyboardButton('Греция')
    australia = types.KeyboardButton('Австралия')
    formentera = types.KeyboardButton('о. Форментера')
    # определили каждую переменную к кнопке и назвали её
    keyboard.add(cuba, georgia, bali, morocco, taiwan, seychelles, portugal, norway, greece, australia, formentera)
    #  зарегистрировали кнопки
    bot.send_message(message.chat.id, 'Сделайте выбор',
                     reply_markup=keyboard)

    # сообщение от бота (с id чата, 'само сообщение', и прикрепление кнопки)
    @bot.message_handler(content_types=['text'])  # content_types=['text'] - отслеживание ввода текста пользователем
    def countries(message):
        if message.text == 'Грузия':
            web = types.InlineKeyboardMarkup()  # определение типа кнопки
            web.add(
                types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/georgia/'))
            # регистрирование кнопки, название кнопки, и добавление в неё ссылки
            bot.send_message(message.chat.id, 'Про Грузию', reply_markup=web)
            # Сообщение от бота над кнопкой

            mon = types.InlineKeyboardMarkup()
            mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='http://www.finmarket.ru/currency/rates/?id=10122&ysclid=l5p7ldbx6o773804645'))
            bot.send_message(message.chat.id, 'Курсы валют в Грузии', reply_markup=mon)


        elif message.text == 'Куба':
            web = types.InlineKeyboardMarkup()
            web.add(
                types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/cuba/?ysclid=l5wzis8cmg680871554'))
            bot.send_message(message.chat.id, 'Про Кубу', reply_markup=web)
            mon = types.InlineKeyboardMarkup()
            mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='https://nashaplaneta.net/asia/indonesia/money?ysclid=l5pffd65fj327741919'))
            bot.send_message(message.chat.id, 'Вторая кнопка', reply_markup=mon)
        elif message.text == 'Бали':
            web = types.InlineKeyboardMarkup()
            web.add(
                types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/indonesia/ostrov-bali/'))
            bot.send_message(message.chat.id, 'Про Индонезию,о.Бали', reply_markup=web)
            mon = types.InlineKeyboardMarkup()
            mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='https://nashaplaneta.net/asia/indonesia/money?ysclid=l5pffd65fj327741919'))
            bot.send_message(message.chat.id, 'Вторая кнопка', reply_markup=mon)
        elif message.text == 'Марокко':
            web = types.InlineKeyboardMarkup()
            web.add(
                types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/morocco/?ysclid=l5wzf2acx4499429891'))
            bot.send_message(message.chat.id, 'Про Марокко', reply_markup=web)
            mon = types.InlineKeyboardMarkup()
            mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='https://nashaplaneta.net/asia/indonesia/money?ysclid=l5pffd65fj327741919'))
            bot.send_message(message.chat.id, 'Вторая кнопка', reply_markup=mon)
        elif message.text == 'Тайвань':
            web = types.InlineKeyboardMarkup()
            web.add(
                types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/china/tayvan/?ysclid=l5wzhmovi5667907437'))
            bot.send_message(message.chat.id, 'Про Тайвань', reply_markup=web)
            mon = types.InlineKeyboardMarkup()
            mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='https://nashaplaneta.net/asia/indonesia/money?ysclid=l5pffd65fj327741919'))
            bot.send_message(message.chat.id, 'Вторая кнопка', reply_markup=mon)
        elif message.text == 'Сейшелы':
            web = types.InlineKeyboardMarkup()
            web.add(
                types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/seychelles/?ysclid=l5wzk27hxx222121054'))
            bot.send_message(message.chat.id, 'Про Сейшельские острова', reply_markup=web)
            mon = types.InlineKeyboardMarkup()
            mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='https://nashaplaneta.net/asia/indonesia/money?ysclid=l5pffd65fj327741919'))
            bot.send_message(message.chat.id, 'Вторая кнопка', reply_markup=mon)
        elif message.text == 'Португалия':
            web = types.InlineKeyboardMarkup()
            web.add(
                types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/portugaliya/?ysclid=l5wzlblllr768099767'))
            bot.send_message(message.chat.id, 'Про Португалию', reply_markup=web)
            mon = types.InlineKeyboardMarkup()
            mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='https://nashaplaneta.net/asia/indonesia/money?ysclid=l5pffd65fj327741919'))
            bot.send_message(message.chat.id, 'Вторая кнопка', reply_markup=mon)
        elif message.text == 'Норвегия':
            web = types.InlineKeyboardMarkup()
            web.add(
                types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/norway/?ysclid=l5wzmulkpb471284760'))
            bot.send_message(message.chat.id, 'Про Норвегию', reply_markup=web)
            mon = types.InlineKeyboardMarkup()
            mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='https://nashaplaneta.net/asia/indonesia/money?ysclid=l5pffd65fj327741919'))
            bot.send_message(message.chat.id, 'Вторая кнопка', reply_markup=mon)
        elif message.text == 'Греция':
            web = types.InlineKeyboardMarkup()
            web.add(
                types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/greece/?ysclid=l5wzpg50em126709284'))
            bot.send_message(message.chat.id, 'Про Грецию', reply_markup=web)
            mon = types.InlineKeyboardMarkup()
            mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='https://nashaplaneta.net/asia/indonesia/money?ysclid=l5pffd65fj327741919'))
            bot.send_message(message.chat.id, 'Вторая кнопка', reply_markup=mon)
        elif message.text == 'Австралия':
            web = types.InlineKeyboardMarkup()
            web.add(
                types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/australia/?ysclid=l5wzqsdj8b510599434'))
            bot.send_message(message.chat.id, 'Про Австралию', reply_markup=web)
            mon = types.InlineKeyboardMarkup()
            mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='https://nashaplaneta.net/asia/indonesia/money?ysclid=l5pffd65fj327741919'))
            bot.send_message(message.chat.id, 'Вторая кнопка', reply_markup=mon)
        elif message.text == 'о. Форментера':
            web = types.InlineKeyboardMarkup()
            web.add(
                types.InlineKeyboardButton('Перейти на сайт',
                                           url='https://wikiway.com/spain/ostrov-formentera/?ysclid=l5wzsrej9m470592014'))
            bot.send_message(message.chat.id, 'Про остров Форментера', reply_markup=web)
            mon = types.InlineKeyboardMarkup()
            mon.add(types.InlineKeyboardButton('Перейти на сайт',
                                               url='https://nashaplaneta.net/asia/indonesia/money?ysclid=l5pffd65fj327741919'))
            bot.send_message(message.chat.id, 'Вторая кнопка', reply_markup=mon)

    @bot.message_handler()
    def send_welcome(message: telebot.types.Message):
        bot.reply_to(message, message.text)
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Перезапуск бота"),
    ])

bot.polling(none_stop=True)  # запуск чата на постоянное выполнениеyu