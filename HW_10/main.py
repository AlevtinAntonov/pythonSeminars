import telebot
from my_token import my_token
from func_polinom import polynom_sum

bot = telebot.TeleBot(my_token)

messages = {'start': 'Добро пожаловать\n' \
					 'Наберите /help для просмотра описания программы \n' \
					 '/sum для запуска суммы многочленов',
			'sum_start': 'Sum startВведите первый многочлен',
			'fst': 'Введите первый многочлен',
			'scnd': 'Введите второй многочлен',
			'finish': 'Расчет произведен\n'
					  'Наберите /sum для запуска программы суммы многочленов',
			'help': 'Наберите /start для приветственого сообщения\n'
					'Наберите /sum для запуска программы суммы многочленов'
			}
logger = {}

@bot.message_handler(commands=['start'])
def start_command(message):
	bot.send_message(message.chat.id, messages['start'])

@bot.message_handler(commands=['help'])
def help_command(message):
	bot.send_message(message.chat.id, messages['help'])

@bot.message_handler(commands=['sum'])
def fst_num(message):
	logger[message.chat.id] = []
	msg = bot.send_message(message.chat.id, messages['fst'])
	bot.register_next_step_handler(msg, scnd_num)

def scnd_num(message):
	logger[message.chat.id].append(message.text)
	msg = bot.send_message(message.chat.id, messages['scnd'])
	bot.register_next_step_handler(msg, sum_calc)

def sum_calc(message):
	logger[message.chat.id].append(message.text)
	print(logger)
	bot.send_message(message.chat.id, polynom_sum(logger[message.chat.id][0], logger[message.chat.id][1]))
	logger[message.chat.id].clear()
	bot.send_message(message.chat.id, messages['finish'])



# bot.infinity_polling()
bot.polling(none_stop=True, interval=0)