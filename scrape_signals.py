from telethon.sync import TelegramClient
import pandas as pd
import datetime

import configparser
config = configparser.ConfigParser()
config.read("config.ini")

api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

groups = ['https://t.me/BinanceLiquidations']

client = TelegramClient(username, api_id, api_hash)

df = pd.DataFrame()


for group in groups:
    with TelegramClient(username, api_id, api_hash) as client:
        for message in client.iter_messages(group, offset_date=datetime.date.today(), reverse=True):
            print(message)
            data = {"group": group, "sender": message.sender_id, "text": message.text, "date": message.date}

            temp_df = pd.DataFrame(data, index=[1])
            df = pd.concat([df, temp_df])

df['date'] = df['date'].dt.tz_localize(None)

df.to_excel("C:\\Users\\zahar\\Desktop\\crypto-web\\crypto-web-app\\data\\data_{}.xlsx".format(datetime.date.today()), index=False)
