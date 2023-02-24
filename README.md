### Описание проекта:

Cбор информации о  количестве статусов PEP(выводит таблицу с колонками "Количество" и "Статус")

### Автор: [Артём Носов](https://github.com/avnosov3)

### Техно-стек:
* python 3.7.9
* scrapy 2.5.1

### Как запустить парсер:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:avnosov3/scrapy_parser_pep.git
```

Cоздать и активировать виртуальное окружение:

```
1. python3 -m venv env
2. source venv/bin/activate
```

Установить зависимости из файла requirements.txt

```
1.python3 -m pip install --upgrade pip
2. pip install -r requirements.txt
```

Запуска парсера

```
scrapy crawl pep
```

Парсер сохранит два файла в директории **/results**    
* pep_<ДАТА>.csv - список всех PEP
* status_summary_<ДАТА>.csv - сводная таблица по количеству статусов