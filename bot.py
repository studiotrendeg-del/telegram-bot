import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ البوت شغال 24 ساعة!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"أنت قلت: {message.text}")

print("🚀 البوت شغال...")
bot.polling()
