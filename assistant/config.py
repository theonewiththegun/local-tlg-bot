import os
import json

with open(os.environ['SECRETS_JSON']) as handle:
    SECRETS = json.loads(handle.read())

TLG_BOT_TOKEN = SECRETS['TLG_BOT_TOKEN']
