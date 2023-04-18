from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

from assistant import config as cfg

bot = (
    ApplicationBuilder()
    .token(cfg.TLG_BOT_TOKEN)
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
