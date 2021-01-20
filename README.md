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
- [x] тесты
- [x] скачивать html на диск (do not download it again)
- [x] получать ссылки с помощью html.parse (bs4)
- [x] работа с `robots.txt`
- [x] не использовать scrapy
- [x] многопоточное скачивание (модель производитель-потребитель)
- [x] исправить принты
- [x] константу вынести в отдельный файл с настройками
- [x] setUp в тестах
- [x] уметь задавать и применять параметры
  - [x] путь для скачивания ссылок
  - [x] количество потоков
  - [x] аргументы для задания правил перехода (текущий домен, группа доменов, зона, ...)
- [x] восстановление работы после сбоя (the ability to resume (store the state))

## Authors
* **Xenia Evdokimova** ([xxeniaev](https://github.com/xxeniaev))
