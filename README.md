# Scrapy parser PEP

Асинхронный парсинг документации Python.
Парсер сохранит два файла в директории **/results**    
* pep_<ДАТА>.csv - список всех PEP
* status_summary_<ДАТА>.csv - сводная таблица по количеству статусов

## Техно-стек
* python 3.7.9
* scrapy 2.5.1

## Как запустить парсер
1. Клонировать репозиторий
```
git@github.com:avnosov3/Scrapy_parser_pep.git
```
2. Перейти в папку с проектом и создать виртуальное окружение

```
cd Scrapy_parser_pep
```
```
python3 -m venv env
python -m venv venv (Windows)
```
3. Активировать виртуальное окружение
```
source env/bin/activate
source venv/Scripts/activate (Windows)
```
4. Установить зависимости из файла requirements.txt
```
pip3 install -r requirements.txt
pip install -r requirements.txt (Windows)
```
5. Запустить парсер
```
scrapy crawl pep
```

## Автор
[Артём Носов](https://github.com/avnosov3)
