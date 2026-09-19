import os
from flask import Flask, request
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Hola! Soy tu bot Goyes, ya estoy 24/7 en Render funcionando.")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, f"Recibi: {m.text}")

@app.route('/webhook', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200

@app.route('/')
def home():
    return "Bot activo!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
