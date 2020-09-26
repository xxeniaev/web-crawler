import uuid
import re
import urllib.request
from bs4 import BeautifulSoup


class HTMLPage:
    """Объект хтмл страницы"""
    def __init__(self, path: str):
        self.__content = self.__readPage(path)
        self.__links = self.__getLinks()

    def __getLinks(self):
        """Поиск всех ссылок на странице, заключенных в тег <href>.
        Достает ссылки начинающиеся ТОЛЬКО на https://, добавить потом поддержку http://."""
        links = []
        for link in self.__content.find_all('a', attrs={"href": re.compile("https://")}):
            links.append(link.get("href"))
        return links

    def __readPage(self, path: str):
        """Парсинг содержимого скачанной страницы"""
        with open(path, "r", encoding="utf-8") as webpage:
            source = webpage.read()
            soup = BeautifulSoup(source, features="html.parser")
        return soup

    @property
    def content(self):
        """Геттер. Выводит форматированный контент страницы."""
        return self.__content.prettify()

    @property
    def links(self):
        """Геттер. Возвращает все найденные ссылки на странице."""
        return self.__links

    @classmethod
    def fromURL(cls, url: str):
        """'Фабрика классов', создает обьект стрницы по заданному url."""
        filename = f"{uuid.uuid4()}.html"
        # Скачиваем файл в текущую папку
        urllib.request.urlretrieve(url, filename)
        return cls(filename)
