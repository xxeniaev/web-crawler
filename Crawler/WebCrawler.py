import re
import os
import settings
import time

from .ArgParser import ArgParser
from .HTMLPage import HTMLPage

import urllib.robotparser as robot
import threading
from queue import Queue


def consumer(q):
    while True:
        page = q.get()
        try:
            page.scrape(q)
        finally:
            q.task_done()


class WebCrawler:
    """Парсинг аргументов, старт скрэппинга"""

    def __init__(self):
        self.start_url = ArgParser().parse_args().start_url
        self.domain = self.get_domain_name()

        self.rp = robot.RobotFileParser(url='')
        self.rp.set_url(self.domain + "/robots.txt")
        self.rp.read()

    def start(self):
        try:
            os.mkdir(settings.DIR)
            os.chdir(settings.DIR)
        except FileExistsError:
            os.chdir(settings.DIR)

        seconds = int(round(time.time()))

        # Producer/consumer pattern
        queue = Queue()

        # turn on the rotate_images thread
        consumers = [threading.Thread(
            target=consumer, args=(queue,), daemon=True) for _ in range(10)]
        for consumer_item in consumers:
            consumer_item.start()

        html_page = HTMLPage(self.start_url, 1, self.rp)
        queue.put(html_page)

        # block until all tasks are done
        queue.join()
        print('All work completed', round(time.time()) - seconds, "sec")

    def get_domain_name(self):
        pattern = re.compile(r'(\w+://\w+\.\w+/)')
        return pattern.search(self.start_url).group()
