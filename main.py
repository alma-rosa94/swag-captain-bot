from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(chat_id, text):
    requests.post(
        f"{TELEGRAM_URL}/sendMessage",
        json={"chat_id": chat_id, "text": text}
    )


@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "Swag Captain is running"

    data = request.get_json()

    if not data or "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "").lower()

    if text in ["/start", "start"]:
        reply = """Welcome to Swag Captain 🧢

I can help with CapSwag retail operations:
• product transfers
• register change reminders
• cleaning checklists
• sales spreadsheet review
• store reminders
• Philly sports merch prep

CapSwag is retail only. For custom apparel or bulk orders, send customers to SwagTex."""

    elif text in ["/help", "help", "what can you do", "what do you do"]:
        reply = """I’m here to help with daily CapSwag store operations.

You can ask me things like:
• “Remind me to transfer Eagles hats from Berlin to OC”
• “What’s the cleaning checklist?”
• “We need change for the register”
• “Help me make a product transfer”
• “Customer wants custom shirts”
• “What should we feature for Philly sports?”"""

    elif "custom" in text or "bulk" in text or "embroidery" in text or "screen print" in text or "uniform" in text:
        reply = """CapSwag is retail only.

For custom apparel, uniforms, bulk orders, embroidery, or screen printing, please send them to SwagTex."""

    elif "transfer" in text or "/transfer" in text:
        reply = """Got it — let’s make a product transfer.

Please send me:
1. Item name or SKU
2. From store: Berlin, OC, or WW
3. To store: Berlin, OC, or WW
4. Quantity
5. Reason if you know it

Example:
Transfer 12 Eagles hats from Berlin to OC because OC is low."""

    elif "clean" in text or "/cleaning" in text:
        reply = """Today’s cleaning checklist:

• Sweep/vacuum floor
• Wipe counters
• Dust hat displays
• Straighten racks
• Restock bags and receipt paper
• Take out trash
• Check fitting/front areas
• Make sure displays look full"""

    elif "change" in text or "register" in text or "/change" in text:
        reply = """Register change reminder:

Please confirm:
1. Store location
2. Register number
3. Amount of change needed
4. Who is handling it

Reminder: keep register coverage in place."""

    elif "sales" in text or "spreadsheet" in text or "/sales" in text:
        reply = """I can help review sales spreadsheets.

For now, upload or export:
• item/SKU
• store location
• quantity on hand
• units sold
• date range

Then I can help suggest transfers between Berlin, OC, and WW."""

    elif "sports" in text or "eagles" in text or "phillies" in text or "sixers" in text or "flyers" in text:
        reply = """Philly sports reminder 🏈⚾🏀🏒

Check front displays for:
• Eagles gear
• Phillies hats/shirts
• Sixers items
• Flyers orange/black items

Before big games, move related merch closer to the front."""

    elif "remind" in text or "/remind" in text:
        reply = """Got it — I can help format the reminder.

Send it like this:
“Remind me tomorrow to transfer Phillies hats from Berlin to OC.”

For real automatic reminders, we’ll add the reminder database next."""

    elif "hi" in text or "hello" in text or "hey" in text:
        reply = "Hey! I’m Swag Captain 🧢 What retail operation do you need help with today?"

    else:
        reply = """I can help with that.

Is this about:
• a product transfer
• register change
• cleaning
• sales spreadsheet
• Philly sports merch
• SwagTex/custom order referral

Tell me what’s going on and I’ll help organize it."""

    send_message(chat_id, reply)
    return "ok"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
