import COVID19Py
import telebot

api_bot = '5085841962:AAHaIzzpvsvpr9tCHnNeyMV-ICH5Xr3m_Wk'
bot = telebot.TeleBot(api_bot)
covid19 = COVID19Py.COVID19()


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b> Привет, {message.from_user.first_name}!</b>\nВведите страну"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

bot.polling(none_stop=True)


#country = input()
#latest = covid19.getLatest()
#location = covid19.getLocationByCountryCode(country)

