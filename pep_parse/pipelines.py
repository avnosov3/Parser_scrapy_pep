import csv
import datetime as dt
from collections import Counter

from pep_parse.settings import BASE_DIR, RESULTS

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_NAME = 'status_summary_{}.csv'


class PepParsePipeline:
    STATUSES = []

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.STATUSES.append(item['status'])
        return item

    def close_spider(self, spider):
        excepted_statuses = Counter(self.STATUSES)
        with open(BASE_DIR / RESULTS / FILE_NAME.format(
            dt.datetime.now().strftime(DATETIME_FORMAT)
        ), 'w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows([
                ('Статус', 'Количество'),
                *excepted_statuses.items(),
                ('Всего', sum(excepted_statuses.values()))
            ])
