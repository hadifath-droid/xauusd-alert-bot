from flask import Flask
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
