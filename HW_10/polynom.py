import telebot
from my_token import my_token
from func_polynom import polynom_sum, convert

bot = telebot.TeleBot(my_token)

messages = {'start': 'Добро пожаловать\n' \
                     'Выберите в меню действие:\n'
                     '/help описание действий\n'
                     '/run запуск программы суммы многочленов',
            'run': 'Введите первый многочлен Next второй многочлен Enter',
            'help': 'Наберите первый многочлен с переменной Х и нажмите Next\n'
                    'Наберите второй многочлен с переменной Х и нажмите Enter\n'
                    'Программа вычислит сумму двух многочленов'
            }
value = ''
old_value = ''
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('C', callback_data='C'),
             telebot.types.InlineKeyboardButton('<=', callback_data='<='),
             telebot.types.InlineKeyboardButton('X', callback_data='x'),
             telebot.types.InlineKeyboardButton('^', callback_data='^'),
             telebot.types.InlineKeyboardButton('/', callback_data='/'))

keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('*', callback_data='*'))

keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('-', callback_data='-'))

keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton('+', callback_data='+'))

keyboard.row(telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton('=', callback_data='='),
             telebot.types.InlineKeyboardButton('Next', callback_data='#'),
             telebot.types.InlineKeyboardButton('Enter', callback_data='##'))

polynom = []


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, messages['start'])


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, messages['help'])


@bot.message_handler(commands=['run'])
def getMessage(message):
    global value
    if value == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    '''Сумма многочлена'''
    global value, old_value
    data = query.data

    if data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value) - 1]

    elif data == '#':
        try:
            polynom.append(convert(value))
            print(f'1 {polynom}')
            value = ''
        except:
            value = 'Ошибка!'
    elif data == '##':
        try:
            polynom.append(convert(value))
            print(f'2 {polynom}')
            value = polynom_sum(polynom[0], polynom[1])
            print(f'3 {value}')
            polynom.clear()
        except:
            value = 'Ошибка!'

    else:
        value += data

    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0',
                                  reply_markup=keyboard)
            old_value = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=value,
                                  reply_markup=keyboard)
            old_value = value


if value == 'Ошибка!':
    value = ''

bot.polling(none_stop=False, interval=0)
