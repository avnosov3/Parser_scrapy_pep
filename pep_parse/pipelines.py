import pathlib
import datetime as dt
import csv

EXPECTED_STATUSES = {
    'Active': 0,
    'Accepted': 0,
    'Deferred': 0,
    'Final': 0,
    'Provisional': 0,
    'Rejected': 0,
    'Superseded': 0,
    'Withdrawn': 0,
    'Draft': 0,
    'April Fool!': 0
}

BASE_DIR = pathlib.Path(__file__).parent
RESULTS = 'results'
RESULTS_DIR = BASE_DIR / RESULTS
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_NAME = 'status_summary_{}.csv'


class PepParsePipeline:

    def open_spider(self, spider):
        RESULTS_DIR.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        EXPECTED_STATUSES[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(BASE_DIR / FILE_NAME.format(
            dt.datetime.now().strftime(DATETIME_FORMAT)
        ), 'w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect
            ).writerows([
                ('Статус', 'Количество'),
                *EXPECTED_STATUSES.items(),
                ('Всего', sum(EXPECTED_STATUSES.values()))
            ])
