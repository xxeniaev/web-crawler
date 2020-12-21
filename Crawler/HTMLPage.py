import os
import re
import urllib.request
from bs4 import BeautifulSoup


class HTMLPage:
    """Объект хтмл страницы"""
    def __init__(self, path: str, nesting: int):
        self.url = path
        self.__nesting = nesting

    def scrape(self):
        """Основной меотд поиска ссылок."""
        if self.__nesting > 3:
            return
        filename = self.get_file_name()
        if not os.path.exists(filename):
            print(self.url, self.__nesting)
            try:
                print(filename)
                urllib.request.urlretrieve(self.url, filename)
                content = self.read_page(filename)
                links = self.get_links(content)
                for link in links:
                    html_page = HTMLPage(link, self.__nesting + 1)
                    html_page.scrape()
            except Exception:
                print('bad url')
                exit(1)

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
        print(links)
        return links
