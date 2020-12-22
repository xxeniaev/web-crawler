# web_crawler
extracting data from websites.
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
  * `HTMLPage.py` parsing pages, getting links and html files, then scrapping
  * `WebCrawler.py` starting crawling
## Future versions
- [x] tests
- [x] download html to disk (do not download it again)
- [x] get links using html.parse (bs4)
- [x] working with `robots.txt` 
- [ ] download in multipe streams (producer-consumer model)'
- [ ] the ability to resume (store the state)
- [x] links within the specified domains 
- [x] don't use scrapy
## Authors
* **Xenia Evdokimova** ([xxeniaev](https://github.com/xxeniaev))
