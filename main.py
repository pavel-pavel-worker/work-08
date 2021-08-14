from pyrogram import Client, filters, types
from datetime import datetime
import os

api_id = os.getenv('APP_API_ID')
api_hash = os.getenv('APP_API_HASH')
channel_id = os.getenv('CHANNEL_ID')
donor_id = os.getenv('DONOR_CHANNEL_ID')
backdoor_id = os.getenv('BACKDOOR_ID')

app = Client('whale pumps admin', api_id, api_hash)


@app.on_message(filters.chat([int(donor_id), int(backdoor_id)]))
def get_post(_, message: types.Message):
    text = message.text
    print('Post was got', text.splitlines()[0])
    if 'on Binance' in text and 'DOWN/' not in text and 'UP/' not in text:
        app.send_message(channel_id, text)
        print('Message was sent to channel')
    elif '123qwe' == text:
        app.send_message(backdoor_id, 'ok')


if __name__ == '__main__':
    print(datetime.today().strftime(f'%H:%M:%S | WhaleBot Pumps Parser launched'))
    app.run()
