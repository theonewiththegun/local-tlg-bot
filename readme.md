# Блюпринт локального сервера ботовской апихи телеграма + бот, который с ним общается

### Как запустить
1. В `./secrets` нужно закинуть `config.json` такого содержания:
    ```json
    {
      "TLG_BOT_TOKEN": "тут ботовский токен"
    }
    ```
2. В `./docker/bot-api-server` нужно закинуть `.env` такого содержания:
    ```dotenv
    TELEGRAM_API_ID=<тут айди аппки>
    TELEGRAM_API_HASH=<тут апи ключ>
    TELEGRAM_STAT=1
    TELEGRAM_LOCAL=1
    ```
   Взять два параметра выше можно тут: https://my.telegram.org/apps

