import os
import re
import urllib.request
import settings
import sys
import logging
import datetime

from bs4 import BeautifulSoup
from queue import Queue

import urllib.robotparser as robot


class HTMLPage:
    """Объект html страницы"""

    def __init__(self, url: str, nesting: int):
        self.url = url
        # вложенность
        self.__nesting = nesting

    def scrape(self, query: Queue):
        """Основной меотод поиска ссылок."""
        if self.__nesting > settings.NESTING:
            return
        filename = self.get_file_name()
        if not os.path.exists(filename):
            logging.basicConfig(level=logging.INFO)
            logging.info(f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} {self.url} {self.__nesting}")
            try:
                urllib.request.urlretrieve(self.url, filename)
            except Exception:
                sys.stderr.write('url is broken\n')
        try:
            content = read_page(filename)
            links = get_links(content)
            dict_of_rp = dict()
            for link in links:
                domain = get_domain_name(link)
                if domain in settings.DOMAINS:
                    if domain not in dict_of_rp:
                        rp = robot.RobotFileParser(url='')
                        rp.set_url(domain + "/robots.txt")
                        rp.read()
                        dict_of_rp[domain] = rp
                    cur_rp = dict_of_rp[domain]
                    if cur_rp.can_fetch("*", link):
                        html_page = HTMLPage(link, self.__nesting + 1)
                        query.put(html_page)
                else:
                    continue
        except FileNotFoundError:
            sys.stderr.write('url was broken\n')

    def get_file_name(self):
        return f"{self.url.replace('https://', '').replace('/', '_')}.html"


def read_page(path: str):
    """Парсинг содержимого скачанной страницы"""
    with open(path, "r", encoding="utf-8") as webpage:
        source = webpage.read()
        soup = BeautifulSoup(source, features="html.parser")
    return soup


def get_links(content):
    """Поиск всех ссылок на странице, заключенных в тег <href>."""
    links = []
    for link in content.find_all(
            'a', attrs={"href": re.compile("https://")}):
        links.append(link.get("href"))
    for link in content.find_all(
            'a', attrs={"href": re.compile("http://")}):
        links.append(link.get("href"))
    return links


def get_domain_name(url):
    pattern = re.compile(r'(\w+://\w+\.\w+/)*')
    return pattern.search(url).group()
