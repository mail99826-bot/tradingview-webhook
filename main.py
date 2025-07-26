from flask import Flask, request
from pybit.unified_trading import HTTP
import os

app = Flask(__name__)

# Получаем ключи из переменных окружения
API_KEY = os.getenv("ZGlayyvdyYTc4LnPe2")
API_SECRET = os.getenv("iNLu56CT9prRfKVTtDP42UR7ZAxx9vQ3CwBn")

# Инициализация клиента Bybit testnet
client = HTTP(
    testnet=True,
    api_key=API_KEY,
    api_secret=API_SECRET
)

@app.route('/', methods=['GET'])
def index():
    return 'Server is running!'

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("Получен сигнал:", data)
    signal = data.get('text', '').upper()  # предполагаем, что в TradingView отправляем в поле "text" команды BUY или SELL

    if signal == "BUY":
        response = client.place_order(
            category="linear",
            symbol="BTCUSDT",
            side="Buy",
            order_type="Market",
            qty=0.01,
            time_in_force="GoodTillCancel"
        )
        print("Buy order:", response)
    elif signal == "SELL":
        response = client.place_order(
            category="linear",
            symbol="BTCUSDT",
            side="Sell",
            order_type="Market",
            qty=0.01,
            time_in_force="GoodTillCancel"
        )
        print("Sell order:", response)
    else:
        print("Неизвестный сигнал")

    return {'status': 'ok'}
