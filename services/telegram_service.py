import os
from dotenv import load_dotenv

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_API_URL = os.getenv("BASE_API_URL")


def start(update, context):
    response_message = "=^._.^="
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=response_message
    )


def http_cats(update, context):
    context.bot.sendPhoto(
        chat_id=update.effective_chat.id, photo=BASE_API_URL + context.args[0]
    )


def unknown(update, context):
    response_message = "Meow? =^._.^="
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=response_message
    )


def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("http", http_cats))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    print("press CTRL + C to cancel.")
    main()