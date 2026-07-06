import logging
import os
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Enable logging so you can see errors/activity in Railway logs
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Read bot token from environment variable (set this in Railway, never hardcode it)
BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "👋 Hi! I'm Word Counter Bot.\n\n"
        "Just send me any text and I'll count:\n"
        "• Words\n"
        "• Characters (with & without spaces)\n"
        "• Sentences\n"
        "• Paragraphs\n\n"
        "Try it now — paste some text!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Just send me a message with any text, and I'll reply with word/character/sentence counts.\n\n"
        "Commands:\n"
        "/start - Welcome message\n"
        "/help - This help message"
    )


def count_text(text: str) -> dict:
    words = text.split()
    chars_with_spaces = len(text)
    chars_without_spaces = len(text.replace(" ", "").replace("\n", "").replace("\t", ""))
    # Split into sentences by ./!/? followed by space or end of string
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    sentences = [s for s in sentences if s.strip()]
    # Paragraphs are separated by one or more blank lines
    paragraphs = [p for p in text.split("\n\n") if p.strip()]

    return {
        "words": len(words),
        "chars_with_spaces": chars_with_spaces,
        "chars_without_spaces": chars_without_spaces,
        "sentences": len(sentences) if text.strip() else 0,
        "paragraphs": len(paragraphs) if paragraphs else (1 if text.strip() else 0),
    }


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    stats = count_text(text)

    reply = (
        f"📊 *Text Stats*\n\n"
        f"📝 Words: {stats['words']}\n"
        f"🔤 Characters (with spaces): {stats['chars_with_spaces']}\n"
        f"🔡 Characters (no spaces): {stats['chars_without_spaces']}\n"
        f"📖 Sentences: {stats['sentences']}\n"
        f"📄 Paragraphs: {stats['paragraphs']}"
    )
    await update.message.reply_text(reply, parse_mode="Markdown")


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is not set!")

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    logger.info("Bot starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
