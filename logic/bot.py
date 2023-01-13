from telethon import TelegramClient, events

from logic.sender import *


def telegram_parser(send_message_func=None, loop=None):
    client = TelegramClient(TELEGRAM_PHONE_NUMBER, TELEGRAM_API_ID, TELEGRAM_API_HASH, loop=loop)
    client.start()

    @client.on(events.NewMessage())
    async def handler(event):
        if send_message_func is None:
            send(event)
        else:
            await send_message_func(f'@prime1\n{event.raw_text}')

    return client
