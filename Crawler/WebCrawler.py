from .ArgParser import ArgParser
from .HTMLPage import HTMLPage


class WebCrawler:
    """Парсинг аргументов, старт скрэппинга"""
    def __init__(self):
        self.__args = ArgParser().parse_args()
        self.nesting = 3

    def start(self):
        html_page = HTMLPage(self.__args.start_url, 1)
        html_page.scrape()
        # scraper = PageScrapper(self.__args.start_url)
        # scraper.scrape()
