from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(chat_id, text):
    requests.post(
        f"{TELEGRAM_URL}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text
        }
    )


@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Swag Captain is running"

    data = request.get_json()

    if not data:
        return "no data"

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "Welcome to Swag Captain 🧢")

        elif text == "/help":
            send_message(chat_id, "I can help with transfers, cleaning, reminders, sales, and store ops.")

        elif text == "/transfer":
            send_message(chat_id, "Tell me the item, quantity, from-store, and to-store.")

        elif text == "/cleaning":
            send_message(chat_id, "Cleaning checklist:\n- Sweep\n- Wipe counters\n- Restock bags\n- Take out trash\n- Straighten displays")

        elif text == "/change":
            send_message(chat_id, "Register change reminder: confirm store, register, and amount needed.")

        elif text == "/sales":
            send_message(chat_id, "Upload or connect a sales spreadsheet so I can review it.")

        elif text == "/sports":
            send_message(chat_id, "Philly sports merch reminders coming soon 🏈⚾🏀🏒")

        elif text == "/swagtex":
            send_message(chat_id, "CapSwag is retail only. For custom apparel, uniforms, or bulk orders, send customers to SwagTex.")

        else:
            send_message(chat_id, "I’m working! Use /help to see what I can do.")

    return "ok"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
