from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

from assistant import config as cfg

bot = (
    ApplicationBuilder()
    .token(cfg.TLG_BOT_TOKEN)
    .base_url(cfg.BOT_API_SERVER_URL)
    .base_file_url(cfg.BOT_API_FILE_URL)
    .local_mode(True)
    .build()
)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        update.message.text
    )


bot.add_handler(
    MessageHandler(
        filters=filters.ALL,
        callback=echo
    )
)
