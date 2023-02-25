import re

import scrapy

from pep_parse.items import PepParseItem

NUMBER_NAME_PATTERN = r'PEP\s(?P<number>\d+)\W+(?P<name>.+)$'

DOMAIN = 'peps.python.org'


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [DOMAIN]
    start_urls = [f'https://{DOMAIN}/']

    def parse(self, response):
        for link in response.css(
            '#numerical-index tbody tr a::attr(href)'
        ).getall():
            yield response.follow(
                link,
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
