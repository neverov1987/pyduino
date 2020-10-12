To build:
docker build -t telebot_and_arduino .

To run:
docker run -v /dev:/dev --privileged -d telebot_and_arduino

Send your Telegram bot /help or /start for view commands

version 0.1
Arduino can ON or OFF led on board by telegramm bot.
Relay assignments not defined.
Status command connect to arduino and get status of all proframmed switches.
