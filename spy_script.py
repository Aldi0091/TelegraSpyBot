import asyncio
from datetime import datetime
from telethon import TelegramClient, events
from telethon.tl.types import UserStatusOnline, UserStatusOffline
from time import sleep
import random


DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
API_HASH = ''
API_ID =
BOT_TOKEN = ''
USER_NAME = ''

client = TelegramClient('data_thief', API_ID, API_HASH)


client.start()
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


@bot.on(events.NewMessage(pattern='^/start$'))
async def start(event):
    counter = 0
    while True:

        account = await client.get_entity('') # set username here without '@'
        await asyncio.sleep(random.uniform(6, 8))
        if isinstance(account.status, UserStatusOnline):
            last_online = datetime.now()
            if counter < 0:
                await event.respond(f"contact went online by: {last_online.strftime(DATETIME_FORMAT)}")
                counter += 1
                await asyncio.sleep(random.uniform(6, 8))

        elif isinstance(account.status, UserStatusOffline):
            last_online = datetime.now()
            if counter >= 0:
                await event.respond(f"By: {last_online.strftime(DATETIME_FORMAT)} contact went offline")
                counter = counter - 1

                await asyncio.sleep(random.uniform(6, 8))


print('client is running')


def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
     main()