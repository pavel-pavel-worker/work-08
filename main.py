from pyrogram import Client, filters, types
from datetime import datetime
from config import APP_API_HASH, APP_API_ID, CHANNEL_ID, DONOR_CHANNEL_ID
import os

# api_id = os.getenv('APP_API_ID')
# api_hash = os.getenv('APP_API_HASH')
api_id = APP_API_ID
api_hash = APP_API_HASH
channel_id = CHANNEL_ID
donor_id = DONOR_CHANNEL_ID

app = Client('bot_python', api_id, api_hash)


@app.on_message(filters.chat(int(donor_id)))
def get_post(_, message: types.Message):
    text = message.text
    if 'on Binance' in text and 'DOWN/' not in text and 'UP/' not in text:
        app.send_message(channel_id, text)


if __name__ == '__main__':
    print(datetime.today().strftime(f'%H:%M:%S | WhaleBot Pumps Parser launched'))
    app.run()
