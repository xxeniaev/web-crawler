from .PageScrapper import PageScrapper
from .ArgParser import ArgParser


class WebCrawler:
    """Парсинг аргументов, старт скрэппинга"""
    def __init__(self):
        self.__args = ArgParser().parse_args()

    def start(self):
        scraper = PageScrapper(self.__args.start_url)
        scraper.scrape()
