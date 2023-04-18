from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    CommandHandler,
    filters
)
from loguru import logger

from assistant import config as cfg

app = (
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


async def grab_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info('Entered the `grab_file` handler.')
    file_obj = await update.message.reply_to_message.document.get_file()
    logger.info(f'Retrieved the file object: `{file_obj}`.')
    file_path = await file_obj.download_to_drive()

    msg_text = f'The file has been saved to `{file_path}`.'
    logger.info(msg_text)
    await update.message.reply_text(msg_text)


app.add_handlers([
    MessageHandler(
        filters=filters.ALL & ~filters.COMMAND,
        callback=echo
    ),
    CommandHandler(
        command='grab',
        callback=grab_file
    ),
])
