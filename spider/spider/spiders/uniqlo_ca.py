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
        # https://www.uniqlo.com/ca/api/commerce/v3/en/cms?path=/women
        json_response = json.loads(response.body_as_unicode())
        status = json_response['status']
        if status == 'ok':
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
                    accordion_list_item_url = item['url']
                    url = f'{self.base_url}cms?path={accordion_list_item_url}'
                    yield scrapy.Request(url, callback=self.parse_accordion_list_item)

    def parse_accordion_list_item(self, response):
        # https://www.uniqlo.com/ca/api/commerce/v3/en/cms?path=/women/outerwear/ultra-light-down
        json_response = json.loads(response.body_as_unicode())
        status = json_response['status']
        if status == 'ok':
            properties = json_response['result']['properties']
            genders_id = properties['gendersId']
            classes_id = properties['classesId']
            title = properties['title']
            category_id = properties['categoryId']
            url = f'{self.base_url}products?path=,,{category_id}&limit=24&offset=0'
            yield scrapy.Request(url, callback=self.parse_product_list)

    def parse_product_list(self, response):
        # https://www.uniqlo.com/ca/api/commerce/v3/en/products?path=,,475&limit=24&offset=0
        json_response = json.loads(response.body_as_unicode())
        status = json_response['status']
        if status == 'ok':
            result = json_response['result']
            offset = result['pagination']['offset']
            items = result['items']
            for item in items:
                product_id = item['productId']
                url = f'{self.base_url}products/{product_id}'
                yield scrapy.Request(url, callback=self.parse_product)

            next_list_url = f'{response.url.rsplit("=")[0]}{offset}'
            yield scrapy.Request(next_list_url, callback=self.parse_product_list)

    def parse_product(self, response):
        json_response = json.loads(response.body_as_unicode())
        status = json_response['status']
        if status == 'ok':
            item = json_response['result']['items'][0]
