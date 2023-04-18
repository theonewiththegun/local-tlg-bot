import os
import json

with open(os.environ['SECRETS_JSON']) as handle:
    SECRETS = json.loads(handle.read())

TLG_BOT_TOKEN = SECRETS['TLG_BOT_TOKEN']

BOT_API_PROTO = 'http://'
BOT_API_SERVER_HOST = os.environ['LOCAL_BOT_API_SERVER_HOST']
BOT_API_SERVER_PORT = os.environ['LOCAL_BOT_API_SERVER_PORT']

BOT_API_SERVER_URL = (
        BOT_API_PROTO
        + BOT_API_SERVER_HOST
        + ':' + BOT_API_SERVER_PORT
        + '/bot'
)
BOT_API_FILE_URL = (
        BOT_API_PROTO
        + BOT_API_SERVER_HOST
        + ':' + BOT_API_SERVER_PORT
        + '/file/bot'
)
