import os
from telegram.ext import Updater, MessageHandler, Filters
from pybit.unified_trading import HTTP

API_KEY = os.getenv("BYBIT_API_KEY")
API_SECRET = os.getenv("BYBIT_API_SECRET")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

client = HTTP(testnet=True, api_key=API_KEY, api_secret=API_SECRET)

def handle_message(update, context):
    text = update.message.text.upper()

    if text == "BUY":
        response = client.place_order(
            category="linear",
            symbol="BTCUSDT",
            side="Buy",
            order_type="Market",
            qty=0.01,
            time_in_force="GoodTillCancel"
        )
        update.message.reply_text(f"BUY order sent: {response}")
    elif text == "SELL":
        response = client.place_order(
            category="linear",
            symbol="BTCUSDT",
            side="Sell",
            order_type="Market",
            qty=0.01,
            time_in_force="GoodTillCancel"
        )
        update.message.reply_text(f"SELL order sent: {response}")
    else:
        update.message.reply_text("Unknown command. Send BUY or SELL.")

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
