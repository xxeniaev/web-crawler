from Crawler import WebCrawler

"""Запуск - python3 main.py https://sitechecker.pro/website-crawler/.
Рекурсивно выведет все ссылки."""

if __name__ == '__main__':
    crawler = WebCrawler()
    crawler.start()
