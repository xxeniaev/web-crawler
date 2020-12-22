from .HTMLPage import HTMLPage

import unittest
import os


html_page = HTMLPage('https://sitechecker.pro/website-crawler/', 1,
                     'https://sitechecker.pro/')
html_page.scrape()


class WebCrawlerTest(unittest.TestCase):
    def test_get_file_name(self):
        filename = html_page.get_file_name()

        self.assertIsNotNone(filename)
        self.assertEqual(filename, 'sitechecker.pro_website-crawler_.html')

    def test_read_page(self):
        filename = html_page.get_file_name()
        contents = html_page.read_page(filename)

        self.assertIsNotNone(contents)

    def test_get_links(self):
        filename = html_page.get_file_name()
        contents = html_page.read_page(filename)
        links = html_page.get_links(contents)

        self.assertIsNotNone(links)

    def test_scrape(self):
        filename = html_page.get_file_name()

        self.assertTrue(os.path.exists(filename))
