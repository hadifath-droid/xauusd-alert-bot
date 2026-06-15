from flask import Flask, request
import os
import requests

app = Flask(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


@app.route("/")
def home():
    return "XAUUSD Alert Bot Running"


@app.route("/send-test")
def send_test():

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": "🚀 TEST SUCCESS\n\nRailway berhasil kirim pesan ke Telegram!"
    }

    requests.post(url, json=payload)

    return "Message Sent"


@app.route("/tv-test")
def tv_test():

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": "📈 TradingView Test Alert\n\nXAUUSD\nTF: M2\nHarga: 4380"
    }

    requests.post(url, json=payload)

    return "TradingView Test Sent"


@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_data(as_text=True)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": data
    }

    requests.post(url, json=payload)

    return "OK", 200


@app.route("/routes")
def routes():

    route_list = []

    for rule in app.url_map.iter_rules():
        route_list.append(str(rule))

    return "<br>".join(route_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
