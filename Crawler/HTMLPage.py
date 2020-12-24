import os
import re
import urllib.request

from bs4 import BeautifulSoup


class HTMLPage:
    CONST = 1

    """Объект html страницы"""
    def __init__(self, url: str, nesting: int, domain, rp):
        self.url = url
        # вложенность
        self.__nesting = nesting
        self.domain = domain
        self.rp = rp

    def scrape(self):
        """Основной меотд поиска ссылок."""
        if self.__nesting > self.CONST:
            return
        filename = self.get_file_name()
        if not os.path.exists(filename):
            print(self.url, self.__nesting)
            try:
                urllib.request.urlretrieve(self.url, filename)
            except Exception:
                print('bad url')
        try:
            content = self.read_page(filename)
            links = self.get_links(content)
            for link in links:
                if self.domain in link:
                    if self.rp.can_fetch("*", link):
                        html_page = HTMLPage(link, self.__nesting + 1,
                                             self.domain, self.rp)
                        html_page.scrape()
                else:
                    continue
        except FileNotFoundError:
            print('it was bad url')

    def get_file_name(self):
        return f"{self.url.replace('https://', '').replace('/', '_')}.html"

    def read_page(self, path: str):
        """Парсинг содержимого скачанной страницы"""
        with open(path, "r", encoding="utf-8") as webpage:
            source = webpage.read()
            soup = BeautifulSoup(source, features="html.parser")
        return soup

    def get_links(self, content):
        """Поиск всех ссылок на странице, заключенных в тег <href>.
        Достает ссылки начинающиеся ТОЛЬКО на https://,
        добавить потом поддержку http://."""
        links = []
        for link in content.find_all(
                'a', attrs={"href": re.compile("https://")}):
            links.append(link.get("href"))
        for link in content.find_all(
                'a', attrs={"href": re.compile("http://")}):
            links.append(link.get("href"))
        return links
