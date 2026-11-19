
import os
import random
import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

logging.basicConfig(level=logging.INFO)

def create_card():
    columns = [
        random.sample(range(1, 16), 5),
        random.sample(range(16, 31), 5),
        random.sample(range(31, 46), 5),
        random.sample(range(46, 61), 5),
        random.sample(range(61, 76), 5)
    ]

    columns[2][2] = "FREE"

    card = " B    I    N    G    O\n"
    card += "---------------------\n"

    for row in range(5):
        card += " ".join(
            str(columns[col][row]).center(5)
            for col in range(5)
        ) + "\n"

    return card

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎱 MESFIN BINGO\n"
        "እንኳን ደህና መጡ!\n"
        "Welcome to MESFIN BINGO!\n\n"
        "/play - የBingo ካርድ ለማግኘት"
    )

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    card = create_card()

    await update.message.reply_text(
        "🎉 የእርስዎ Bingo Card\n"
        "Your Bingo Card:\n\n"
        f"<pre>{card}</pre>",
        parse_mode="HTML"
    )

def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN is missing")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))

    print("MESFIN BINGO is running!")

    app.run_polling()

if __name__ == "__main__":
    main()
