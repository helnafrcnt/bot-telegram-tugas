import telebot
import datetime

api = '1227263764:AAFBjGITuyGs9aMMBt-ST_hm9p6wIwsOSeM'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def action_start(message):
    nama = message.from_user.first_name
    nomor_id = message.from_user.id
    usernam = message.from_user.username
    bot.reply_to(message,'Selamat Datang di Pertemuan 10. \n Halo {} \n  ID = {} \n username = {}'.format(nama,nomor_id,usernam))
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,'hubungi ke @helnafrcnt')

@bot.message_handler(content_types=['document'])
def kirim_file(message):
    nama = message.from_user.first_name
    file_name = message.document.file_name
    raw = message.document.file_id
    file_info = bot.get_file(raw)
    tanggal = datetime.datetime.now()
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name,'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message,'Terimakasih {} ,sudah mengirimkan file {} pada = {} '.format(nama,file_name,tanggal))

print("bot running")
bot.polling()