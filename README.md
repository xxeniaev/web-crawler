# web_crawler
highlights mistakes in texts and corrects them.
## Getting Started
just download the program from here :)
### Requirements
* `beautifulsoup4` (installing by pip)
## Usage
### Notes
* first and the most important argument is url.
* use `--help` or `-h` for help ***(optional).***
### Examples
```
python3 main.py https://sitechecker.pro/website-crawler/
```
## Modules
* `main.py` launching
* Crawler
  * `ArgParser.py` spellchecking
  * `HTMLPage.py` parsing pages, getting links and html files
  * `PageScrapper.py` scrapping pages
  * `WebCrawler.py` starting crawling
## Future versions
* working with `robots.txt`
* download in multipe streams (producer-consumer model)'
* the ability to resume (store the state)
## Authors
* **Xenia Evdokimova** ([xxeniaev](https://github.com/xxeniaev))
