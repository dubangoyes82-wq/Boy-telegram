import os
from flask import Flask, request
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Hola! Soy tu bot Goyes, ya estoy activo!")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, f"Recibi: {m.text}")

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "ok", 200
    return "error", 403

@app.route('/')
def home():
    return "Bot activo!", 200
