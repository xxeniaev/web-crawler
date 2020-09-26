import argparse


class ArgParser(argparse.ArgumentParser):
    """Парсер аргументов.
    Первый, обязательный аргумент - адресс сайта,
    Второй, опциональный, - [-h, --help], выведет вспомогательное сообщение."""
    def __init__(self):
        super().__init__()

        self.description = 'WebCrawler [OPTIONS] <START-URL>.\n\t' \
                           'Get all links recursively from web pages.\n\t'

        self.add_argument("start_url", nargs='?', help="web page URL to start from")