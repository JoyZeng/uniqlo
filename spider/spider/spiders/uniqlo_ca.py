# -*- coding: utf-8 -*-
import scrapy
import json
from urllib.parse import urlparse

class UniqloCaSpider(scrapy.Spider):
    name = 'uniqlo_ca'
    allowed_domains = ['uniqlo.com/ca']
    start_urls = [
        'https://www.uniqlo.com/ca/api/commerce/v3/en/cms?path=%2Fwomen',
        'https://www.uniqlo.com/ca/api/commerce/v3/en/cms?path=%2Fmen',
        'https://www.uniqlo.com/ca/api/commerce/v3/en/cms?path=%2Fkids',
        'https://www.uniqlo.com/ca/api/commerce/v3/en/cms?path=%2Fbaby'
    ]

    def parse(self, response):
        json_response = json.loads(response.body_as_unicode())
        body = json_response['result']['body']

        # Get category navigation
        for item in body:
            if item['_type'] == 'CategoryGridWithNav':
                category_nav = item['navContent']
                break

        # Get category accordions
        for item in category_nav:
            if item['_type'] == 'List' and item['type'] == 'borderedList':
                accordions = item['children']
                break
            
        # Get category accordion list items
        for accordion in accordions:
            accordion_type = accordion['headingText']
            list_items = accordion['children']['children']
            for item in list_items:
                accordion_list_item_type = item['label']
                accordion_list_item_url = item['url']
                url = urlparse.urljoin(response.url, accordion_list_item_url)
                print(url)

