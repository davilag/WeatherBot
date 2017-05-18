#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from message_consumer.message_consumer import MessageConsumer
import logging, os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

consumer = MessageConsumer();


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text('I will send your weather forecast if you send me your location.\n\n'
                                'You can also control me by sending this commands: \n'
                                '/rain - After sending your location I will send you a summary of today\'s rain probability')



def echo(bot, update):
    print(update)
    update.message.reply_text(update.message.text)

def forecast(bot, update):
    update.message.reply_text(consumer.today_forecast(update['message']))

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    TOKEN = os.getenv('TELEGRAM_API_TOKEN', '')
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(consumer.get_rain_handler())
    dp.add_handler(MessageHandler(Filters.location, forecast))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
