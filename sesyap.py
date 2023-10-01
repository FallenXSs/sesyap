import telebot
from gtts import gTTS
from io import BytesIO

bot_token = "6086089724:AAELu6YRS_U0JuJMmWPyhtnBMWJ18iOnPRY"
bot = telebot.TeleBot(6086089724:AAELu6YRS_U0JuJMmWPyhtnBMWJ18iOnPRY)

@bot.message_handler(commands=['ses']) # /ses komutuna cevap veren fonksiyon
def convert_to_speech(message):
    cmd, *text = message.text.split(" ", 1)
    
    if len(text) != 1: # Eğer metin girilmemişse
        bot.reply_to(message, "Metin girilmemiş!")
        return
    
    tts = gTTS(text[0], lang='tr') # Girilen metni sese dönüştür
    audio = BytesIO()
    tts.save(audio)
    audio.seek(0)
    bot.send_audio(message.chat.id, audio) # Ses dosyasını kullanıcıya gönder

bot.polling()
