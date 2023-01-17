from telethon import TelegramClient, events

from logic.sender import *


def telegram_parser(logging, send_message_func=None, loop=None):
    client = TelegramClient(TELEGRAM_PHONE_NUMBER, TELEGRAM_API_ID, TELEGRAM_API_HASH, loop=loop)
    client.start()

    @client.on(events.NewMessage())
    async def handler(event):

        if send_message_func is None:
            try:
                channelData = await client.get_entity(event.message.peer_id.channel_id)
                if not event.photo:
                    image = "none"
                else:
                    image = await client.download_media(event.photo, "img/test")
                send(channelData.username, event, image, logging)
            except AttributeError:
                pass
        else:
            await send_message_func(f'@prime1\n{event.raw_text}')

    return client
