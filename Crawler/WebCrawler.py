import re

from .ArgParser import ArgParser
from .HTMLPage import HTMLPage

import urllib.robotparser as urobot
import urllib.request


class WebCrawler:
    """Парсинг аргументов, старт скрэппинга"""
    def __init__(self):
        self.__args = ArgParser().parse_args()
        self.domain = self.get_domain_name()
        self.rp = urllib.robotparser.RobotFileParser(url='')
        self.rp.set_url(self.domain + "/robots.txt")
        self.rp.read()

    def start(self):
        html_page = HTMLPage(self.__args.start_url, 1, self.domain, self.rp)
        html_page.scrape()

    def get_domain_name(self):
        pattern = re.compile(r'(\w+://\w+\.\w+/)')
        return pattern.search(self.__args.start_url).group()
