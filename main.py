from pyrogram import Client, filters, types
from datetime import datetime
import os
# from config import APP_API_HASH, APP_API_ID, CHANNEL_ID, DONOR_CHANNEL_ID

api_id = os.getenv('APP_API_ID')
api_hash = os.getenv('APP_API_HASH')
channel_id = os.getenv('CHANNEL_ID')
donor_id = os.getenv('DONOR_CHANNEL_ID')
# api_id = APP_API_ID
# api_hash = APP_API_HASH
# channel_id = CHANNEL_ID
# donor_id = DONOR_CHANNEL_ID

app = Client('whale pumps admin', api_id, api_hash)


# @app.on_message(filters.chat([donor_id, int(channel_id)]))
@app.on_message(filters.chat([int(donor_id), int(channel_id)]))
def get_post(_, message: types.Message):
    print('Post was got')
    text = message.text
    if 'on Binance' in text and 'DOWN/' not in text and 'UP/' not in text:
        app.send_message(channel_id, text)
        print('Message was sent to channel')


if __name__ == '__main__':
    print(datetime.today().strftime(f'%H:%M:%S | WhaleBot Pumps Parser launched'))
    app.run()
