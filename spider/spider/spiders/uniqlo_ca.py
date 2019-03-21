# -*- coding: utf-8 -*-
import scrapy
import json


class UniqloCaSpider(scrapy.Spider):
    name = 'uniqlo_ca'
    allowed_domains = ['uniqlo.com']

    types = ['women', 'men', 'kids', 'baby']
    base_url = 'https://www.uniqlo.com/ca/api/commerce/v3/en/'
    start_urls = [f'https://www.uniqlo.com/ca/api/commerce/v3/en/cms?path=/{type}' for type in types]

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

        # Get category accordion list
        for accordion in accordions:
            accordion_list_type = accordion['headingText']
            accordion_list = accordion['children'][0]['children']
            for item in accordion_list:
                accordion_list_item_type = item['label']
                accordion_list_item_url = item['url']
                url = f'{self.base_url}cms?path={accordion_list_item_url}'
                yield scrapy.Request(url, callback=self.parse_accordion_list_item)

    def parse_accordion_list_item(self, response):
        json_response = json.loads(response.body_as_unicode())
        properties = json_response['result']['properties']
        genders_id = properties['gendersId']
        classes_id = properties['classesId']
        title = properties['title']
        category_id = properties['categoryId']
        print(category_id)

