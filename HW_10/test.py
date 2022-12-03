import telebot
from my_token import my_token
from func_polynom import polynom_sum

bot = telebot.TeleBot(my_token)

messages = {'start': 'Добро пожаловать\n' \
                     'Выберите в меню действие:\n'
                     '/help описание действий\n'
                     '/run запуск программы суммы многочленов',
            'run': 'Введите первый многочлен\n'
                   '(например: 3x^3-2x^2+x-5=0)',
            'scnd': 'Введите второй многочлен\n'
                    '(например: 5x^4+5x^2-7x+15=0)',
            'finish': 'Расчет произведен\n'
                      'Наберите /run для запуска программы суммы многочленов',
            'help': 'Наберите /start для приветственого сообщения\n'
                    'Наберите /run для запуска программы\n'
                    'Введите многочлены в формате:\n'
                    '3x^3-2x^2+x-5=0'
            }
logger = {}


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, messages['start'])


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, messages['help'])


@bot.message_handler(commands=['run'])
def fst_num(message):
    logger[message.chat.id] = []
    msg = bot.send_message(message.chat.id, messages['run'])
    # logger[message.chat.id].append(message.txt)
    # print(logger)
    bot.register_next_step_handler(msg, scnd_num)


def scnd_num(message):
    logger[message.chat.id].append(message.text)
    print(logger)
    msg = bot.send_message(message.chat.id, messages['scnd'])

    bot.register_next_step_handler(msg, sum_calc)


def sum_calc(message):
    logger[message.chat.id].append(message.text)
    print(logger)
    result = bot.send_message(message.chat.id, polynom_sum(logger[message.chat.id][0], logger[message.chat.id][1]))
    logger[message.chat.id].append(str(result))
    print(logger)
    # logger[message.chat.id].clear()
    bot.send_message(message.chat.id, messages['finish'])


# bot.infinity_polling()
bot.polling(none_stop=True, interval=0)
