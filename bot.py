import os
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

MENU = [
    ["📅 Сабақ кестесі"],
    ["📚 Кітап іздеу және әдебиеттер"],
    ["🏢 Ғимараттар мен аудиториялар"],
    ["🏫 Университет туралы ақпарат"],
]

LINKS = {
    "📅 Сабақ кестесі": (
        "Сабақ кестесін мына сілтемеден көре аласыз:",
        "https://wkatu.edu.kz/ru/raspisanie-zanyatij/"
    ),
    "📚 Кітап іздеу және әдебиеттер": (
        "Электрондық кітапханаға өту үшін төмендегі сілтемені басыңыз:",
        "https://elib.wkau.kz/"
    ),
    "🏢 Ғимараттар мен аудиториялар": (
        "Ғимараттар мен аудиторияларға қатысты ақпаратты осы сайттан қараңыз:",
        "https://wkatu.edu.kz/ru/raspisanie-zanyatij/"
    ),
    "🏫 Университет туралы ақпарат": (
        "Университет туралы ақпаратты мына сілтемеден қараңыз:",
        "https://wkatu.edu.kz/ru/raspisanie-zanyatij/"
    ),
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(
        MENU, resize_keyboard=True
    )
    await update.message.reply_text(
        "Сәлем, студент! 👋\n"
        "Мен — University Navigator KZ.\n"
        "Қажетті бөлімді таңдаңыз:",
        reply_markup=keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text.strip()

    if choice in LINKS:
        message, url = LINKS[choice]
        buttons = InlineKeyboardMarkup([[
            InlineKeyboardButton("🔗 Сайтты ашу", url=url)
        ]])
        await update.message.reply_text(message, reply_markup=buttons)
    else:
        await update.message.reply_text(
            "Қажетті ақпаратты алу үшін төмендегі мәзірден бөлімді таңдаңыз."
        )

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN орнатылмаған")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )
    app.run_polling()

if __name__ == "__main__":
    main()
