from .HTMLPage import HTMLPage


class PageScrapper:
    def __init__(self, start_url: str):
        self.__startURL = start_url
        self.__visitedLinks = set()

    def scrape(self):
        """Основной меотд поиска ссылок."""
        start_page = HTMLPage.fromURL(self.__startURL)
        for link in start_page.links:
            if link not in self.__visitedLinks:
                self.__visitedLinks.add(link)

                # Чтобы был виден прогресс
                print(self.__visitedLinks)
                self.scrape()

    @property
    def visitedLinks(self):
        """Возвращает список посещенных ссылок.
        Вывести конечный результат."""
        return self.__visitedLinks
