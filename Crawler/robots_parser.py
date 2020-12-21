import re
from urllib.request import urlopen
import codecs


class RobotsParser:
    def __init__(self, url: str):
        self.url_to_robots_file = get_robots_file(url)

    def get_allowed_links(self):
        pass

    def load(self):
        try:
            with urlopen(self._link) as response:
                html_response = response.read()
                contents = codecs.decode(html_response, 'utf8')
        except PermissionError:
            print('probably you don\'t have permission for opening '
                  'this document')
            exit(1)
        except UnicodeDecodeError:
            print('problems with decoding')
            exit(1)
        except Exception:
            print('probably you don\'t have internet connection')
            exit(1)
        else:
            dictionary = set()
            dictionary.update(contents.split())


def get_robots_file(url):
    pattern = re.compile(r'(\w+://\w+\.\w+/)')
    domain = pattern.search(url).group()
    # print(domain + 'robots.txt/')
    return domain + 'robots.txt/'
