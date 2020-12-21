import os
import uuid
import re
import urllib.request
from bs4 import BeautifulSoup


class HTMLPage:
    """Объект хтмл страницы"""
    def __init__(self, path: str, nesting):
        self.__links = []
        self.url = path
        self.__nesting = nesting

    def __getLinks(self, content):
        """Поиск всех ссылок на странице, заключенных в тег <href>.
        Достает ссылки начинающиеся ТОЛЬКО на https://,
        добавить потом поддержку http://."""
        links = []
        for link in content.find_all(
                'a', attrs={"href": re.compile("https://")}):
            links.append(link.get("href"))
        return links

    def __readPage(self, path: str):
        """Парсинг содержимого скачанной страницы"""
        with open(path, "r", encoding="utf-8") as webpage:
            source = webpage.read()
            soup = BeautifulSoup(source, features="html.parser")
        return soup

    @property
    def links(self):
        """Геттер. Возвращает все найденные ссылки на странице."""
        return self.__links

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
                content = self.__readPage(filename)
                links = self.__getLinks(content)
                for link in links:
                    html_page = HTMLPage(link, self.__nesting + 1)
                    html_page.scrape()
            except:
                print('bad url')

    def get_file_name(self):
        return f"{self.url.replace('https://', '').replace('/', '_')}.html"
