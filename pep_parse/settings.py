import pathlib

from pep_parse.spiders.pep import PepSpider

BOT_NAME = 'pep_parse'
MODULE = 'pep_parse.spiders'

SPIDER_MODULES = [MODULE]
NEWSPIDER_MODULE = MODULE

BASE_DIR = pathlib.Path(__file__).parent
RESULTS = 'results'
FORMAT = 'csv'

ROBOTSTXT_OBEY = True

FEEDS = {
    f'{RESULTS}/{PepSpider.name}_%(time)s.csv': {
        'format': FORMAT,
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
