import os
import re
import urllib.request
import settings
import sys
import logging
import datetime

from bs4 import BeautifulSoup


class HTMLPage:
    """Объект html страницы"""

    def __init__(self, url: str, nesting: int, rp):
        self.url = url
        # вложенность
        self.__nesting = nesting
        self.rp = rp

    def scrape(self):
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
            for link in links:
                # print('weird ', link)
                domain = get_domain_name(link)
                # print('ppp ', get_domain_name(link))
                if domain in settings.DOMAINS and self.rp.can_fetch("*", link):
                    html_page = HTMLPage(link, self.__nesting + 1, self.rp)
                    html_page.scrape()
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
    # print('weird ', url)
    pattern = re.compile(r'(\w+://\w+\.\w+/)*')
    # print(pattern.search(url))
    return pattern.search(url).group()
