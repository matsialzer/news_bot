from logic.bot import *

if __name__ == "__main__":
    client = telegram_parser()
    client.run_until_disconnected()
