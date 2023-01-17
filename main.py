import logging
from logic.bot import *

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")
    client = telegram_parser(logging)
    client.run_until_disconnected()
