"""Код для python. Выполнение команды ардуино поличенных через телеграм бота"""
import serial
import time
import telebot

# telegram bot init
bot = telebot.TeleBot(${{ secrets.TELEBOT_TOKEN }})

# Назначаем порт для связи с Arduino
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)


# Назаначяаем команды для телебота
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, мои доступные команды \n'
                                      '/start для вывода этого сообщения \n'
                                      '/help для справки \n'
                                      '/LED_ON for ON led \n'
                                      '/LED_OFF for OFF led \n'
                                      '/RELAY_1_ON for ON relay 1 \n'
                                      '/RELAY_1_OFF for OFF relay 1 \n'
                                      '/STATUS for STATUS led \n'
                                      '')


# Справка по командам для телебота
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, мои доступные команды \n'
                                      '/start для вывода этого сообщения \n'
                                      '/help для справки \n'
                                      '/LED_ON for ON led \n'
                                      '/LED_OFF for OFF led \n'
                                      '/RELAY_1_ON for ON relay 1 \n'
                                      '/RELAY_1_OFF for OFF relay 1 \n'
                                      '/STATUS for STATUS led \n'
                                      '')


# Команда включения светодиода
@bot.message_handler(commands=['LED_ON'])
def led_on(message):
    """/LEB_ON, бот отдаст команду 1 в порт ардуины, а ардуина в свою очередь выполнить необходимое действие"""
    bot.send_message(message.chat.id, 'Ок. LED_ON')
    arduino_on = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
    arduino_on.write(b'1')
    arduino_on.close()


# Команда выключения светодиода
@bot.message_handler(commands=['LED_OFF'])
def led_off(message):
    """/LEB_OFF, бот отдаст команду 1 в порт ардуины, а ардуина в свою очередь выполнить необходимое действие"""
    bot.send_message(message.chat.id, 'Ок. LED_OFF')
    arduino_off = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
    arduino_off.write(b'0')
    arduino_off.close()


# Команда включения реле 1
@bot.message_handler(commands=['RELAY_1_ON'])
def relay_1_on(message):
    bot.send_message(message.chat.id, 'Ок. RELAY_1_ON')
    arduino_on = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
    arduino_on.write(b'2')
    arduino_on.close()


# Команда выключения реле 1
@bot.message_handler(commands=['RELAY_1_OFF'])
def relay_1_off(message):
    bot.send_message(message.chat.id, 'Ок. RELAY_1_OFF')
    arduino_off = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
    arduino_off.write(b'3')
    arduino_off.close()


# Запрос состояния светодиода и реле
@bot.message_handler(commands=['STATUS'])
def status(message):
    """при получении команды /STATUS бот отдаст информацию о текщем состоянии переключателей"""
    arduino_status = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)
    arduino_status.write(b'9')
    time.sleep(2)
    data = arduino_status.readline()[:-2]  # Получение списка состояния переключателей (флагов) от ардуино
    data = data.decode()  # расшифровка из bytes
    data = data.strip()  # удаление лишних символов
    data = list(data)  # преобразование строки в список
    print(data)
    if data:  # проверка на отсутствие данных
        if len(data) < 5:  # проверка корректности массива
            bot.send_message(message.chat.id, 'Wrong data from arduino')
            return
        elif len(data) > 5:  # проверка корректности массива
            bot.send_message(message.chat.id, 'Wrong data from arduino')
            return
        else:
            print(len(data))
            print("data OK")
        print(type(data))
        """Подготовленные сообщения (default)
        """
        message_0 = 'LED OFF'
        message_1 = 'RELAY_1 OFF'
        message_2 = 'RELAY_2 OFF'
        message_3 = 'RELAY_3 OFF'
        for x in range(0, len(data)):
            if data[x] == "1" and x == 0:
                message_0 = 'LED ON'  # сообещние в случае если диод включен
            if data[x] == "1" and x == 1:
                message_1 = 'RELAY_1 ON'  # сообещние в случае если реле 1 включено
            if data[x] == "1" and x == 2:
                message_2 = 'RELAY_2 ON'  # сообещние в случае если реле 2 включено
            if data[x] == "1" and x == 3:
                message_3 = 'RELAY_3 ON'  # сообещние в случае если реле 3 включено

        print(message_0)
        print(message_1)
        print(message_2)
        print(message_3)
        tele_message = message_0 + '\n' + message_1 + '\n' + message_2 + '\n' + message_3 + '\n'  # сборка сообщения для
        # отправки
        bot.send_message(message.chat.id, tele_message)  # отправка сообщения STATUS

    arduino_status.close()


bot.polling()

