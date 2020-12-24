from .HTMLPage import HTMLPage

import urllib.robotparser as urobot
import urllib.request
import unittest
import os


class WebCrawlerTest(unittest.TestCase):
    def setUp(self):
        self.rp = urllib.robotparser.RobotFileParser(url='')
        self.rp.set_url("https://sitechecker.pro/robots.txt")
        self.rp.read()

        self.html_page = HTMLPage('https://sitechecker.pro/website-crawler/', 1,
                             'https://sitechecker.pro/', self.rp)
        self.html_page.scrape()

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
