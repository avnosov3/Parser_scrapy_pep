import csv
import datetime as dt

from scrapy.exceptions import DropItem

from pep_parse.settings import BASE_DIR, RESULTS

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_NAME = 'status_summary_{}.csv'
DUBLICATE_MESSAGE = 'Найдена повторяющееся запись: "{}"'


class PepParsePipeline:

    def __init__(self):
        self.numbers_seen = set()
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)
        self.statuses = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        number = item['number']
        status = item['status']
        if number in self.numbers_seen:
            raise DropItem(DUBLICATE_MESSAGE.format(item))
        self.numbers_seen.add(number)
        self.statuses[status] = self.statuses.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        with open(self.results_dir / FILE_NAME.format(
            dt.datetime.now().strftime(DATETIME_FORMAT)
        ), 'w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows([
                ('Статус', 'Количество'),
                *self.statuses.items(),
                ('Всего', sum(self.statuses.values()))
            ])
