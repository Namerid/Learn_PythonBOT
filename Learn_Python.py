import telebot
from telebot import types
from time import sleep
import config 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):

	sti = open('st/sticker.webp','rb')
	bot.send_sticker(message.chat.id,sti)
	
	markup = types.InlineKeyboardMarkup(row_width=1)
	item1 = types.InlineKeyboardButton('Поехали!🚀', callback_data='start0')
	markup.add(item1)

	bot.send_message(message.chat.id, 'Привет, {.first_name}, я бот обучающий python, что будем делать?'.format(message.from_user) , reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)

def choose(call):
	if call.message:
		if call.data == 'start':
			
			markup = types.InlineKeyboardMarkup(row_width = 1)
			item1 = types.InlineKeyboardButton('Урок 0: "Установка Python"', callback_data = '0')
			item2 = types.InlineKeyboardButton('Урок 0.1: "Replit"', callback_data = '0.1')
			item3 = types.InlineKeyboardButton('Урок 1: "Типы данных"', callback_data = '1')
			item4 = types.InlineKeyboardButton('Урок 2: "Константы и переменные"',callback_data = '2')
			item5 = types.InlineKeyboardButton('Урок 2.1: "Правила присваивания имен переменным"',callback_data = '2.1')
			item6 = types.InlineKeyboardButton('Урок 2.2: "Таблица операторов"', callback_data= '2.2')
			item7 = types.InlineKeyboardButton('Урок 3: "Оператор if (Условные инструкции)"', callback_data= '3')
			item8 = types.InlineKeyboardButton('Урок 4: "Функции (встроенные)"',callback_data = '4')
			item9 = types.InlineKeyboardButton('Урок 5: "Оператор while"',callback_data = '5')
			item10 = types.InlineKeyboardButton('Урок 6: "Цикл for"',callback_data = '6')

			markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)

			bot.send_message(call.message.chat.id, 'Выберете урок:', reply_markup = markup)
		
		if call.data == 'start0':
			
			markup = types.InlineKeyboardMarkup(row_width = 1)
			item1 = types.InlineKeyboardButton('Урок 0: "Установка Python"', callback_data = '0')
			item2 = types.InlineKeyboardButton('Урок 0.1: "Replit"', callback_data = '0.1')
			item3 = types.InlineKeyboardButton('Урок 1: "Типы данных"', callback_data = '1')
			item4 = types.InlineKeyboardButton('Урок 2: "Константы и переменные"',callback_data = '2')
			item5 = types.InlineKeyboardButton('Урок 2.1: "Правила присваивания имен переменным"',callback_data = '2.1')
			item6 = types.InlineKeyboardButton('Урок 2.2: "Таблица операторов"', callback_data= '2.2')
			item7 = types.InlineKeyboardButton('Урок 3: "Оператор if (Условные инструкции)"', callback_data= '3')
			item8 = types.InlineKeyboardButton('Урок 4: "Функции (встроенные)"',callback_data = '4')
			item9 = types.InlineKeyboardButton('Урок 5: "Оператор while"',callback_data = '5')
			item10 = types.InlineKeyboardButton('Урок 6: "Цикл for"',callback_data = '6')

			markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
			
			bot.send_message(call.message.chat.id, '''Источники:
			http://www.swaroopch.com/notes/Python''')

			bot.send_message(call.message.chat.id, 'Выберете урок:', reply_markup = markup)	
		
		if call.data == '0':
			bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.message_id, text='Выберерете урок:',
			reply_markup=None)
			bot.send_message(call.message.chat.id, '>>>\n>>>\n>>>')

			bot.send_message(call.message.chat.id, 'Для того, что бы начать работу необходимо установить python')
			sleep(2)
			bot.send_message(call.message.chat.id, 'Скачать можно на официальном сайте: https://www.python.org')
			sleep(3)
			bot.send_photo(call.message.chat.id, open('photo/lesson_1/ptn_org.png','rb'))
			sleep(4)
			bot.send_message(call.message.chat.id, 'Вопрос: "где писать код?"')
			sleep(3)
			bot.send_message(call.message.chat.id, 'Вместе с python идет IDE (среда разработки), пока что этого будет достаточно')
			sleep(4)
			bot.send_message(call.message.chat.id, 'Давайте запустим IDLE. Сначала будет включен интерактивный режим, его основной особеностью является отсутствие сохранения написаного кода')
			sleep(6)
			bot.send_message(call.message.chat.id, 'Напишим свою первую программу: "Привет, Мир!"')
			sleep(4)
			bot.send_message(call.message.chat.id, '''>>>print ("Hello, world")
			Hello, world''')
			sleep(3)
			bot.send_message(call.message.chat.id, 'print - вывести')
			sleep(3)

			markup = types.InlineKeyboardMarkup(row_width = 1)
			item0 = types.InlineKeyboardButton('Другой урок', callback_data = 'start')
			markup.add(item0)

			bot.send_message(call.message.chat.id, 'Сегодня мы прошли первый урок и написали свою первую программу', reply_markup = markup)

		if call.data == '0.1':
			
			bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.message_id, text='Выберерете урок:',
			reply_markup=None)
			bot.send_message(call.message.chat.id, '>>>\n>>>\n>>>')

			bot.send_message(call.message.chat.id, 'Replit - бесплатная онлайн среда разработки')
			sleep(3)
			bot.send_message(call.message.chat.id, 'Для начала работы с Replit необходимо зайти на официальный сайт: https://replit.com')
			sleep(3)
			bot.send_message(call.message.chat.id, 'Нажать кнопку "Start coding"')
			sleep(2)
			bot.send_photo(call.message.chat.id, open('photo/lesson_0.1/start.png','rb'))
			sleep(4)
			bot.send_message(call.message.chat.id, 'Можно зарегистрировать новый аккаунт или войти через google, githab или facebook')
			sleep(2)
			bot.send_photo(call.message.chat.id, open('photo/lesson_0.1/account.png','rb'))
			sleep(3)
			bot.send_message(call.message.chat.id, 'Далее нужно создать repl')
			sleep(2)
			bot.send_photo(call.message.chat.id, open('photo/lesson_0.1/create_repl.png','rb'))
			sleep(4)
			bot.send_message(call.message.chat.id, 'Настраиваем repl (выбираем язык программирования, название файла и т.д)')
			sleep(2)
			bot.send_photo(call.message.chat.id, open('photo/lesson_0.1/settings.png','rb'))
			sleep(4)
			bot.send_message(call.message.chat.id, 'Мы можем поделится проектом')
			sleep(2)
			bot.send_photo(call.message.chat.id, open('photo/lesson_0.1/share.png','rb'))
			sleep(4)

			markup = types.InlineKeyboardMarkup(row_width = 1)
			item0 = types.InlineKeyboardButton('Другой урок', callback_data = 'start')
			markup.add(item0)

			bot.send_message(call.message.chat.id, 'Используйте Replit!', reply_markup = markup)

		if call.data == '1':
			bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.message_id, text='Выберерете урок:',
			reply_markup=None)
			bot.send_message(call.message.chat.id, '>>>\n>>>\n>>>')

			bot.send_message(call.message.chat.id, 'В Python каждое значение, например 2 или "Привет, мир!" называется объектом.')
			sleep(4)
			bot.send_message(call.message.chat.id, '''Рассмотрим объект как значение данных в Python, которое имеет три свойства:
			*Идентификатор
			*Тип данных
			*Значение''')
			sleep(4)
			bot.send_message(call.message.chat.id, 'Идентификатор - место где объект хранится в памяти вашего компьютера, и оно никогда не меняется.')
			sleep(4)
			bot.send_message(call.message.chat.id, '"Привет, мир" - объект с типом данных Str, сокращение от английского слова string - строка, и значением "Привет, мир"')
			sleep(4)
			bot.send_message(call.message.chat.id, 'Строка - последовательность одного или нескольких символов, помещенных в кавычки.')
			sleep(4)
			
			markup = types.InlineKeyboardMarkup(row_width = 1)
			item0 = types.InlineKeyboardButton('Другой урок', callback_data = 'start')
			markup.add(item0)
			
			bot.send_message(call.message.chat.id,'''Таблица
			Тип данных
			
			int = integer - целое число (1, 2, 3, 4 и т.д.)
			
			float - числа с плавающей точкой (1.3, 5.913 и т.д.)
			
			bool - логические, могут быть истнными или ложными (True, False)							
			
			NoneZype используются для представления отсутствия значения, всегда равно "None" (None)''', 
			reply_markup = markup)

		if call.data == '2':
			bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.message_id, text='Выберерете урок:',
			reply_markup=None)
			bot.send_message(call.message.chat.id, '>>>\n>>>\n>>>')

			bot.send_message(call.message.chat.id, '>>>2+2\n4')
			sleep(2)
			bot.send_message(call.message.chat.id, '>>>2-2\n0')
			sleep(2)
			bot.send_message(call.message.chat.id, '>>>2*2\n4')
			sleep(2)
			bot.send_message(call.message.chat.id, 'Константа - это значение, которое никогда не меняется. Каждое из чисел в предыдущем примере будет константой. Число два всегда будет равняться 2.')
			sleep(6)
			bot.send_message(call.message.chat.id, 'Переменная - значение которое может изменяться.')
			sleep(4)
			bot.send_message(call.message.chat.id, 'Присваивание в Python:')
			sleep(3)
			bot.send_message(call.message.chat.id, '>>>b = 100\n>>>b\n100')
			sleep(3)
			bot.send_message(call.message.chat.id, 'Измение переменной:')
			sleep(3)
			bot.send_message(call.message.chat.id, '>>>x = 100\n>>>x\n100\n>>>x = 200\n>>>x\n200')
			sleep(5)
			bot.send_message(call.message.chat.id, 'Увеличение (уменьшение) переменной:')
			sleep(3)
			bot.send_message(call.message.chat.id, '>>>x = 10\n>>>x\n10\n>>>x = x + 1\nx\n11')
			sleep(5)
			bot.send_message(call.message.chat.id, 'Сокращенные вариант:')
			sleep(3)
			
			markup = types.InlineKeyboardMarkup(row_width = 1)
			item0 = types.InlineKeyboardButton('Другой урок', callback_data = 'start')
			markup.add(item0)
			bot.send_message(call.message.chat.id, '>>>x = 10\n>>>x\n10\n>>>x += 1\n>>>x\n11',reply_markup = markup)

		if call.data == '2.1':
			bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.message_id, text='Выберерете урок:',
			reply_markup=None)
			bot.send_message(call.message.chat.id, '>>>\n>>>\n>>>')

			bot.send_message(call.message.chat.id, 'Правила присваивания имен переменным:')
			sleep(2)
			bot.send_message(call.message.chat.id, '*Не могут содержать пробелы')
			sleep(2)
			bot.send_message(call.message.chat.id, '*Имена могут содержать только латинские буквы, цифры, знак подчеркивания(_).')
			sleep(3)
			bot.send_message(call.message.chat.id, '*Имя не должно начинаться с цифры.')
			sleep(3)
			
			markup = types.InlineKeyboardMarkup(row_width = 1)
			item0 = types.InlineKeyboardButton('Другой урок', callback_data = 'start')
			markup.add(item0)
			bot.send_message(call.message.chat.id, '*Нельзя использовать ключевые слова.',reply_markup = markup)

		if call.data == '2.2':
			bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.message_id, text='Выберерете урок:',
			reply_markup=None)
			bot.send_message(call.message.chat.id, '>>>\n>>>\n>>>')

			bot.send_message(call.message.chat.id, 'Таблица операторов:')
			sleep(1)
			bot.send_photo(call.message.chat.id, open('photo/lesson_2.2/table.png','rb'))
			sleep(2)
			
			markup = types.InlineKeyboardMarkup(row_width = 1)
			item0 = types.InlineKeyboardButton('Другой урок', callback_data = 'start')
			markup.add(item0)
			bot.send_message(call.message.chat.id, 'Таблица операторов',reply_markup = markup)

		if call.data == '3':
			bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.message_id, text='Выберерете урок:',
			reply_markup=None)
			bot.send_message(call.message.chat.id, '>>>\n>>>\n>>>')

			bot.send_message(call.message.chat.id, 'Оператор if используется для проверки условий: если условие верно, выполняется блок выражений (называемый «if-блок»), иначе выполняется другой блок выражений (называемый «else-блок»). Блок «else» является необязательным.')
			sleep(7)
			bot.send_message(call.message.chat.id, 'Пример (отдельная программа):')
			sleep(2)
			bot.send_photo(call.message.chat.id, open('photo/lesson_3/program.png','rb'))
			sleep(28)
			bot.send_message(call.message.chat.id, 'Вывод:')
			sleep(2)
			bot.send_message(call.message.chat.id, '''$ python 
Введите целое число : 50
Нет, загаданное число немного меньше этого.
Завершено

$ python 
Введите целое число : 22
Нет, загаданное число немного больше этого.
Завершено

$ python 
Введите целое число : 23
Поздравляю, вы угадали,
(хотя и не выиграли никакого приза!)
Завершено''')
			sleep(10)
			bot.send_message(call.message.chat.id, 'Как это работает:')
			sleep(2)
			bot.send_message(call.message.chat.id, 'В этой программе мы принимаем варианты от пользователя и проверяем, совпадают ли они с заранее заданным числом. Мы устанавливаем переменной number значение любого целого числа, какого хотим. Например, 23. После этого мы принимаем вариант числа от пользователя при помощи функции input(). Функции – это всего-навсего многократно используемые фрагменты программы. Мы узнаем о них больше в следующих уроках.')
			sleep(20)
			bot.send_message(call.message.chat.id, 'Мы передаём встроенной функции input строку, которую она выводит на экран и ожидает ввода от пользователя. Как только мы ввели что-нибудь и нажали клавишу Enter, функция input() возвращает строку, которую мы ввели. Затем мы преобразуем полученную строку в число при помощи int(), и сохраняем это значение в переменную guess. Вообще-то, int – это класс, но на данном этапе вам достаточно знать лишь, что при помощи него можно преобразовать строку в целое число (предполагая, что строка содержит целое число).')
			sleep(24)
			bot.send_message(call.message.chat.id, 'Далее мы сравниваем число, введённое пользователем, с числом, которое мы выбрали заранее. Если они равны, мы печатаем сообщение об успехе. Обратите внимание, что мы используем соответствующие уровни отступа, чтобы указать Python, какие выражения относятся к какому блоку. Вот почему отступы так важны в Python. Я надеюсь, вы придерживаетесь правила «постоянных отступов», не так ли?')
			sleep(20)
			bot.send_message(call.message.chat.id, 'Обратите внимание, что в конце оператора if стоит двоеточие – этим мы показываем, что далее следует блок выражений.')
			sleep(8)
			bot.send_message(call.message.chat.id, 'После этого мы проверяем, верно ли, что пользовательский вариант числа меньше загаданного, и если это так, мы информируем пользователя о том, что ему следует выбирать числа немного больше этого. Здесь мы использовали выражение elif, которое попросту объединяет в себе два связанных if else-if else выражения в одно выражение if-elif-else. Это облегчает чтение программы, а также не требует дополнительных отступов.')
			sleep(20)
			bot.send_message(call.message.chat.id, 'Выражения elif и else также имеют двоеточие в конце логической строки, за которым следуют соответствующие блоки команд (с соответствующим числом отступов, конечно).')
			sleep(10)
			bot.send_message(call.message.chat.id, 'Внутри if-блока оператора if может быть другой оператор if и так далее – это называется вложенным оператором if.')
			sleep(6)
			bot.send_message(call.message.chat.id, 'Помните, что части elif и else не обязательны. Минимальная корректная запись оператора if такова:')
			sleep(5)
			bot.send_message(call.message.chat.id, '''if True:
    print('Да, это верно.')''')
			sleep(3)
			
			markup = types.InlineKeyboardMarkup(row_width = 1)
			item0 = types.InlineKeyboardButton('Другой урок', callback_data = 'start')
			markup.add(item0)
			bot.send_message(call.message.chat.id, 'После того, как Python заканчивает выполнение всего оператора if вместе с его частями elif и else, он переходит к следующему выражению в блоке, содержащем этот оператор if. В нашем случае это основной блок программы (в котором начинается выполнение программы), а следующее выражение – это print("Завершено"). После этого Python доходит до конца программы и просто выходит из неё.',reply_markup = markup)

		if call.data == '4':
			bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.message_id, text='Выберерете урок:',
			reply_markup=None)
			bot.send_message(call.message.chat.id, '>>>\n>>>\n>>>')

			bot.send_message(call.message.chat.id, 'Функция')
			sleep(1)
			bot.send_message(call.message.chat.id, 'Функции – это многократно используемые фрагменты программы. Можно создавать свои функции, а можно пользоваться встроенными. Сейчас мы рассмотрим второй вариант.')
			sleep(6)
			bot.send_message(call.message.chat.id, 'Форма записи функции:')
			sleep(2)
			bot.send_message(call.message.chat.id, 'функция(аргументы)')
			sleep(2)
			bot.send_message(call.message.chat.id, 'Аргументы - объекты переданные функции. Они могуть быть обязательными и необязательными.')
			sleep(4)
			bot.send_message(call.message.chat.id, 'Примеры встроенных функций:')
			sleep(2)
			bot.send_message(call.message.chat.id, 'int() - переводит аргумент в объект с типом int (целое число)')
			sleep(3)
			bot.send_message(call.message.chat.id, 'float() - переводит аргумент в объект с типом float (число с плавающей точкой)')
			sleep(3)
			bot.send_message(call.message.chat.id, 'str() - переводит аргумент в объект с типом string (строка)')
			sleep(3)
			bot.send_message(call.message.chat.id, 'input() - импортирует объект из коммандной строки')
			sleep(3)

			markup = types.InlineKeyboardMarkup(row_width = 1)
			item0 = types.InlineKeyboardButton('Другой урок', callback_data = 'start')
			markup.add(item0)
			bot.send_message(call.message.chat.id, 'print() - выводит объект в коммандную строку',reply_markup = markup)

		if call.data == '5':
			bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.message_id, text='Выберерете урок:',
			reply_markup=None)
			bot.send_message(call.message.chat.id, '>>>\n>>>\n>>>')

			bot.send_message(call.message.chat.id, 'Оператор while')
			sleep(1)
			bot.send_message(call.message.chat.id, 'Оператор while позволяет многократно выполнять блок команд до тех пор, пока выполняется некоторое условие. Это один из так называемых операторов цикла. Он также может иметь необязательный пункт else.')
			sleep(6)
			bot.send_message(call.message.chat.id, 'Пример:')
			sleep(1)
			bot.send_photo(call.message.chat.id, open('photo/lesson_5/program.png','rb'))
			sleep(18)
			bot.send_message(call.message.chat.id, 'Вывод:')
			sleep(1)
			bot.send_message(call.message.chat.id, '''$ python
Введите целое число : 50
Нет, загаданное число немного меньше этого.
Введите целое число : 22
Нет, загаданное число немного больше этого.
Введите целое число : 23
Поздравляю, вы угадали.
Цикл while закончен.
Завершение.''')
			sleep(13)
			bot.send_message(call.message.chat.id, 'Мы продолжаем угадывать числа, но в отличии от предыдущего раза, пользовательлю не нужно запускать программу заново, чтобы попробовать угадать снова. ')
			sleep(7)
			bot.send_message(call.message.chat.id, 'Мы переместили операторы input и if внутрь цикла while и установили переменную running в значение True перед запуском цикла. Прежде всего проверяется, равно ли значение переменной running True, а затем происходит переход к соответствующему while-блоку.')
			sleep(10)
			bot.send_message(call.message.chat.id, 'После выполнения этого блока команд условие, которым в данном случае является переменная running, проверяется снова. Если оно истинно, while-блок запускается снова, в противном случае происходит переход к дополнительному else-блоку, а затем – к следующему оператору.')
			sleep(10)
			bot.send_message(call.message.chat.id, 'Блок else выполняется тогда, когда условие цикла while становится ложным (False) – это может случиться даже при самой первой проверке условия. Если у цикла while имеется дополнительный блок else, он всегда выполняется, если только цикл не будет прерван оператором break.')
			sleep(10)
			
			markup = types.InlineKeyboardMarkup(row_width = 1)
			item0 = types.InlineKeyboardButton('Другой урок', callback_data = 'start')
			markup.add(item0)
			bot.send_message(call.message.chat.id, 'True и False называются булевым типом данных, и вы можете считать их эквивалентными значениям 1 и 0 соответственно.',reply_markup = markup)

		if call.data == '6':
			bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.message_id, text='Выберерете урок:',
			reply_markup=None)
			bot.send_message(call.message.chat.id, '>>>\n>>>\n>>>')

			bot.send_message(call.message.chat.id, 'Цикл for')
			sleep(1)
			bot.send_message(call.message.chat.id, 'Оператор for..in также является оператором цикла, который осуществляет итерацию по последовательности объектов, т.е. проходит через каждый элемент в последовательности. Последовательность – это упорядоченный набор элементов.')
			sleep(8)
			bot.send_message(call.message.chat.id, 'Пример:')
			sleep(1)
			bot.send_photo(call.message.chat.id, open('photo/lesson_6/program.png','rb'))
			sleep(7)
			bot.send_message(call.message.chat.id, 'Как это работает:')
			sleep(1)
			bot.send_message(call.message.chat.id, 'В этой программе мы выводим на экран последовательность чисел. Мы генерируем эту последовательность, используя встроенную функцию range.')
			sleep(5)
			bot.send_message(call.message.chat.id, 'Мы задаём два числа, и range возвращает последовательность чисел от первого числа до второго. Например, range(1,5) даёт последовательность [1, 2, 3, 4]. По умолчанию range принимает значение шага, равное 1. Если мы зададим также и третье число range, оно будет служить шагом. Например, range(1,5,2) даст [1,3]. Помните, интервал простирается только до второго числа, т.е. не включает его в себя.')
			sleep(17)
			bot.send_message(call.message.chat.id, 'Затем цикл for осуществляет итерацию по этому диапазону - for i in range(1,5) эквивалентно for i in [1, 2, 3, 4], что напоминает присваивание переменной i по одному числу (или объекту) за раз, выполняя блок команд для каждого значения i. В данном случае в блоке команд мы просто выводим значение на экран.')
			sleep(15)
			bot.send_message(call.message.chat.id, 'Помните, что блок else не обязателен. Если он присутствует, он всегда выполняется один раз после окончания цикла for, если только не указан оператор break.')
			sleep(7)

			markup = types.InlineKeyboardMarkup(row_width = 1)
			item0 = types.InlineKeyboardButton('Другой урок', callback_data = 'start')
			markup.add(item0)
			bot.send_message(call.message.chat.id, 'Помните также, что цикл for..in работает для любой последовательности. В нашем случае это список чисел, сгенерированный встроенной функцией range, но в общем случае можно использовать любую последовательность любых объектов!',reply_markup = markup)


bot.polling (none_stop=True)
