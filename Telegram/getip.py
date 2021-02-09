import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


TOKEN = "Your_telegram_bot_chat"


def initLogger():
    loglevel = os.getenv('LOGLEVEL', 'INFO')

    # Messager formatter
    fmt = logging.Formatter(
        '%(asctime)s|%(levelname)s|%(name)s|%(message)s',
        '%Y-%m-%d %H:%M:%S'
    )

    ch = logging.StreamHandler()  # Console handler
    ch.setLevel(loglevel)
    ch.setFormatter(fmt)

    rh = logging.handlers.RotatingFileHandler(
        filename='messages.log',
        mode='a',
        maxBytes=2_000_000,
        backupCount=2
    )
    rh.setLevel('INFO')
    rh.setFormatter(fmt)

    LOGGER.setLevel(loglevel)
    LOGGER.addHandler(ch)
    LOGGER.addHandler(rh)


def start(update: Update, context: CallbackContext) -> None:
    msg = 'Use /getip to get hostname and IP address'
    update.message.reply_text(msg)


def getip(update: Update, context: CallbackContext):
    """What is my hostname and IP address"""
    if os.name == 'nt':  cmd = 'ipconfig'
    else:                cmd = 'ip add'
    msg = os.popen(cmd).read()
    update.message.reply_text(msg)


def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("getip", getip))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
