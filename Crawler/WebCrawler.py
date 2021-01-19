import re
import os
import settings

from .ArgParser import ArgParser
from .HTMLPage import HTMLPage

import urllib.robotparser as urobot
import urllib.request


class WebCrawler:
    """Парсинг аргументов, старт скрэппинга"""
    def __init__(self):
        self.start_url = ArgParser().parse_args().start_url
        self.domain = self.get_domain_name()

        self.rp = urllib.robotparser.RobotFileParser(url='')
        self.rp.set_url(self.domain + "/robots.txt")
        self.rp.read()

    def start(self):
        try:
            os.mkdir(settings.DIR)
            os.chdir(settings.DIR)
        except FileExistsError:
            os.chdir(settings.DIR)

        html_page = HTMLPage(self.start_url, 1, self.domain, self.rp)
        html_page.scrape()

    def get_domain_name(self):
        pattern = re.compile(r'(\w+://\w+\.\w+/)')
        return pattern.search(self.start_url).group()
