from assistant.tlg import bot

if __name__ == '__main__':
    bot.bot.log_out()  # to guarantee that the bot won't use the cloud bot api server
    bot.run_polling()
