import os

from telegram import Update, constants
from telegram.helpers import escape_markdown
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    CommandHandler,
    filters,
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
    file_obj = await update.message.reply_to_message.document.get_file()  # that actually downloads the file

    # there seems to be no proper way to retrieve a file path
    # we can get a link, but the files are not served (except when we do this explicitly with an http server),
    # so the link is useless; below i build a path by myself
    # more on serving files and why it does not work in local mode here:
    # https://github.com/tdlib/telegram-bot-api/issues/381
    file_abspath = cfg.LOCAL_FILES_STORE + os.path.basename(file_obj.file_path)
    msg_text = rf'The file has been saved to `{escape_markdown(file_abspath, version=2)}`\.'
    logger.info(msg_text)
    await update.message.reply_text(msg_text, parse_mode=constants.ParseMode.MARKDOWN_V2)


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
