from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder, 
    CommandHandler, 
    ContextTypes, 
    MessageHandler, 
    filters
)
import logging
KEY = "5770895006:AAHDea7u_GMlgCX81ehDJo_FSSv6psqPpl0"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update:Update, content:ContextTypes)->None:
    return await update.message.reply_text("Hello world")

async def help(update:Update, content:ContextTypes)->None:
    return await update.message.reply_text("""
/help - Show this message
/start - Start the bot
""")

async def handle_responses(update:Update, context:ContextTypes) -> str:
    text: str = update.message.text.lower()     
    usename = update.message.from_user.username
    response = ""

    if 'hello' in text:
        response = f'Hello there! {usename} How can i help you? \n'

    if 'how are you' in text:
        response = response + "I`m fine, thank you, And you? \n"

    with open("tablet.png", "rb") as f:
        
        await update.message.reply_photo(f, caption="Hello world!")
    
    return await update.message.reply_text(response)


if __name__ == "__main__":
    app = ApplicationBuilder().token(KEY).build()
    print("Bot is running...")

    #commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_responses))

    # Run the bot
    print("Polling...")
    app.run_polling(poll_interval=1)



