# https://web.telegram.org/a/#7729753936
from bs4 import BeautifulSoup
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

url = "https://uaserials.pro/films/"

r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")

soup_list_href = soup.find_all('a',{"class":"short-img img-fit"})
f = open('link.txt',"w", encoding='utf-8')
for href in soup_list_href:
    # print(href['href'])
    f.write(f"{href['href']}\n")

f.close()
links_list = []
with open('link.txt', 'r') as file:
    links_list = file.readlines()

# print(links_list)
f = open('info.txt', 'w', encoding='utf-8')
list_name = []
list_desc = []
for link in links_list:
    req = requests.get(link)
    soup1 = BeautifulSoup(req.text,features="html.parser" )
    soup_list_name_film = soup1.find_all('span', {"class":"oname_ua"})
    if len(soup_list_name_film)> 0:
        f.write(f'{soup_list_name_film[0].text}\n')
        list_name.append(soup_list_name_film[0].text)
    soup_list_ul = soup1.find_all('ul',{"class":"short-list fx-1"})
    for item in soup_list_ul:
        f.write(f"{item.text}\n")
        list_desc.append(item.text)

f.close()
command = """/help - список всіх команд бота
/hello - привітання,
/film - список найновіших фільмів"""
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def film(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i in range(len(links_list)):
        text = f"{list_name[i]}\n{list_desc[i]}\n{links_list[i]}"
        await update.message.reply_text(text)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(command)


app = ApplicationBuilder().token("7729753936:AAF7pyJEJ1J1WgmdmQWYchBJ5BSFMfT9G6I").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("film", film))
app.add_handler(CommandHandler("help", menu))

app.run_polling()

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from datetime import datetime
import random

# Увімкнення логів
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# 1. /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Я твій телеграм-бот. Напиши /help, щоб побачити команди.")

# 2. /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start — Почати роботу з ботом\n"
        "/help — Допомога\n"
        "/time — Показати поточний час\n"
        "/echo <текст> — Повторити текст\n"
        "/joke — Надіслати жарт"
    )

# 3. /time
async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    await update.message.reply_text(f"Зараз {now}")

# 4. /echo
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        msg = ' '.join(context.args)
        await update.message.reply_text(msg)
    else:
        await update.message.reply_text("Напиши щось після команди /echo")

# 5. /joke
async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = [
        "Чому програмісти не ходять у ліс? Бо бояться багів 🐞",
        "Як називається змія-програміст? Пайтон 🐍",
        "Чому комп’ютер холодний? Бо відкриті всі вікна! 🪟",
    ]
    await update.message.reply_text(random.choice(jokes))

# Запуск бота
if __name__ == '__main__':
    app = ApplicationBuilder().token('YOUR_BOT_TOKEN_HERE').build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("time", time))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("joke", joke))

    print("Бот запущено...")
    app.run_polling()

