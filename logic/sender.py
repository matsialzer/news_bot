import requests

from logic.settings import *


def send(username, event, logging):
    try:
        image = event.photo.id
    except AttributeError:
        image = "none"

    payload = {
        'site': 'telegram',
        'title': 'bot',
        'label': 'bot',
        'body': event.text,
        'source': 'https://t.me/{0}'.format(username),
        'img': image
    }
    files = []
    headers = {'api-key': API_KEY}
    response = requests.request("POST", API_URL, headers=headers, data=payload, files=files)
    logging.info('new event')
    logging.info(response.text)
