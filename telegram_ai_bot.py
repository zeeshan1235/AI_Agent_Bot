import telebot
import os
import requests

TOKEN = "8938319881:AAGf5PIxzuxxwxSXCFv8FVd5jxqYFMdeD5U"
KEY = "AIzaSyBxFMvAkPMtYtQRCnKN1wlZP8XG4z4hz3o"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "AI is coding...")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={KEY}"
    data = {"contents": [{"parts": [{"text": f"Write only python code for: {message.text}"}]}]}
    response = requests.post(url, json=data).json()
    code = response['candidates'][0]['content']['parts'][0]['text'].replace("```python", "").replace("```", "")
    with open("projects/app.py", "w") as f:
        f.write(code)
    os.system("git add . && git commit -m 'Auto' && git push origin main")
    bot.reply_to(message, "Done! Check GitHub.")

bot.polling()
