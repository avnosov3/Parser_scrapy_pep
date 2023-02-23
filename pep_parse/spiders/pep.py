import re

import scrapy

from pep_parse.items import PepParseItem

NUMBER_NAME_PATTERN = r'PEP\s(?P<number>\d+)\W+(?P<name>.+)$'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for row in response.css('#numerical-index tbody tr'):
            yield response.follow(
                row.css('a::attr(href)').get(),
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        number, name = re.search(
            NUMBER_NAME_PATTERN,
            response.css('h1.page-title::text').get()
        ).groups()
        yield PepParseItem({
            'number': number,
            'name': name,
            'status': response.css('abbr::text').get()
        })
