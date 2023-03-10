from telegram import Update
from new import get_profile_info
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(get_profile_info(update.effective_user))    


app = ApplicationBuilder().token("5635774650:AAHEOuzEtmIA0ZXQY81zY7cPqDzGZofSLDQ").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()