from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("Получен сигнал:", data)
    # Тут можно добавить вызов к Bybit API
    return {'status': 'ok'}

