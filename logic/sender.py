import requests
from logic.settings import *


def send(event):
    print("\n ========= new event =========")
    image = 'e'
    try:
        source = 'https://t.me/c/{0}/{1}'.format(event.message.peer_id.channel_id, event.id)
    except AttributeError:
        source = ''
    payload = {
        'title': 'bot',
        'label': 'bot',
        'body': event.text,
        'source': source,
        'img': image
    }
    files = []
    headers = {'api-key': API_KEY}

    response = requests.request("POST", API_URL, headers=headers, data=payload, files=files)
    print(event.text)
    print(response.text)
    print("\n =============================")
