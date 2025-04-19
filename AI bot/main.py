import telebot


# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7961283682:AAEj51zi0608prUDVrBV8cpSvQl3_HZmI2U")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin  ")


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    if not message.photo:
        return bot.send_message(message.chat.id,"gguy" :(""))
    
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]

    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

    
# Запускаем бота
bot.polling()

from logic import detect

print(detect("images/images.jpg"))


path = files.upload()
path = list(path.keys())[0]
image=Image.open(path)

bird = detect(path)
if bird == 'елка':
  print()
if bird == 'дуб':
  print()
if bird == 'береза':
  print()
if bird == 'клен':
  print()