# Scrapy parser PEP
<details><summary>Russian language</summary>  

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
git clone git@github.com:avnosov3/Parser_scrapy_pep.git
```
2. Перейти в папку с проектом и создать виртуальное окружение

```
cd Parser_scrapy_pep
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
</details>

<details><summary>English language</summary>  

Asynchronous parsing Python documentation.
The parser will save two files in the **/results** directory
* pep_<DATE>.csv - list of all PEPs
* status_summary_<DATE>.csv - summary table by the number of statuses

## Stack
* python 3.7.9
* scrapy 2.5.1

## Launch of the project
1. Clone repository
```
git clone git@github.com:avnosov3/Parser_scrapy_pep.git
```
2. Go to the project folder and create a virtual environment
```
cd Parser_scrapy_pep
```
```
python3 -m venv env
python -m venv venv (Windows)
```
3. Activate a virtual environment
```
source env/bin/activate
source venv/Scripts/activate (Windows)
```
4. Install dependencies from requirements.txt
```
pip3 install -r requirements.txt
pip install -r requirements.txt (Windows)
```
5. Run parser
```
scrapy crawl pep
```

## Author
[Artem Nosov](https://github.com/avnosov3)
</details>
