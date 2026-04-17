import os
import random
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ты долбаёб? Нахуй ты сюда пришёл? Скорее всего это твои последние минуты жизни, так что выборов у тебя не много. Въёбывай по кнопки Негр ой точнее хелп потому что ты, долбаёб, сам не справишься.")

async def commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Сука тупое чмо ну ладно вот список команд но ты иди нахуй если че: \n"
        "/start - Я тут блять даже объяснять не буду \n"
        "/help - негр \n"
        "/pohod - пойти нахуй \n"
        "/craft - Наработки Макса \n"
        "/inventory - Посмотреть инвентарь чмошника"
        )

last_day = None
resources = {
    "Помидорчики: ": 0,
    "Веточки: ": 0,
    "Помидорные кусты: ": 0,
    "Крокодил: ": 0,
    "Томатный потрошитель: ": 0,
    "Селитра: ": 0,
    "Помидорные бомбы: ": 0,
    "кпоурп4део3йжлпзАКШВЫПЩОКПЩ: ": 0,

}

async def pohod(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_day
    today = datetime.now().day
    if today == last_day:
        await update.message.reply_text("Ты уже ходил сегодня в поход!")
        return
    else:
        last_day = today
        pomidors = random.randint(0, 5)
        vetochki = random.randint(0, 3)
        await update.message.reply_text(f"Ты отправился в поход и нашел помидор в количестве: {pomidors}, веточек: {vetochki}")
        resources["Помидорчики: "] += pomidors
        resources["Веточки: "] += vetochki

async def craft(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Доступные крафты такому бездарю как ты: \n"
        "Помидорный куст: x10 помидоров, x5 веточек \n"
        "Селитра СКОРО \n"
        "Помидорные бомбы СКОРО \n"
        "Горшочек СКОРО"
    )

async def inventory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Твой инвентарь: \n"
        f"Помидорчики: {resources['Помидорчики: ']} \n"
        f"Веточки: {resources['Веточки: ']}"
    )

async def idle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if resources["Помидорчики: "] >= 10 and resources["Веточки: "] >= 5:
        await update.message.reply_text("Ты скрафтил помидорный куст!")
        resources["Помидорчики: "] -= 10
        resources["Веточки: "] -= 5
        resources["Помидорные кусты: "] += 1
    else:
        await update.message.reply_photo(photo=open("images/c97316ed67af27db8d77948499abddd2.jpg"), "rb")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", commands))
app.add_handler(CommandHandler("pohod", pohod))
app.add_handler(CommandHandler("craft", craft))
app.add_handler(CommandHandler("inventory", inventory))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r".*Помидорный куст.*"), idle))

app.run_polling()
