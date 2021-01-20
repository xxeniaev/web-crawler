from .HTMLPage import HTMLPage

from queue import Queue

import unittest
import os


class WebCrawlerTest(unittest.TestCase):
    def setUp(self):
        try:
            os.mkdir('test_files')
            os.chdir('test_files')
        except FileExistsError:
            os.chdir('test_files')

        queue = Queue()

        self.html_page = HTMLPage('https://sitechecker.pro/website-crawler/', 1)
        self.html_page.scrape(queue)

    def test_get_file_name(self):
        filename = self.html_page.get_file_name()

        self.assertIsNotNone(filename)
        self.assertEqual(filename, 'sitechecker.pro_website-crawler_.html')

    def test_read_page(self):
        filename = self.html_page.get_file_name()
        contents = self.html_page.read_page(filename)

        self.assertIsNotNone(contents)

    def test_get_links(self):
        filename = self.html_page.get_file_name()
        contents = self.html_page.read_page(filename)
        links = self.html_page.get_links(contents)

        self.assertIsNotNone(links)

    def test_scrape(self):
        filename = self.html_page.get_file_name()

        self.assertTrue(os.path.exists(filename))

    def test_get_domain_name(self):
        url = self.html_page.url

        self.assertEqual(self.html_page.get_domain_name(url), 'https://sitechecker.pro/')

    def test_get_zone(self):
        url = self.html_page.url
        domain = self.html_page.get_domain_name(url)

        self.assertEqual(self.html_page.get_zone(domain), '.pro')
