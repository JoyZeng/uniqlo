# -*- coding: utf-8 -*-
import scrapy
import json
from spider.items import UniqloItem


class UniqloCaSpider(scrapy.Spider):
    name = 'uniqlo_ca'
    allowed_domains = ['uniqlo.com']

    base_url = 'https://www.uniqlo.com/ca/api/commerce/v3/en/'
    start_urls = ['https://www.uniqlo.com/ca/api/commerce/v3/en/products?limit=1']

    def get_gender_url(self, gender_id):
        return f'{self.base_url}products?path={gender_id}'

    def get_class_url(self, class_id):
        return f'{self.base_url}products?path=,{class_id}'

    def get_category_url(self, category_id):
        return f'{self.base_url}products?path=,,{category_id}'

    def get_subcategory_url(self, subcategory_id):
        return f'{self.base_url}products?path=,,,{subcategory_id}'

    def get_product_url(self, product_id):
        return f'{self.base_url}products/{product_id}'

    def parse(self, response):
        """
        Get product level 1 category (WOMEN, MEN, KIDS, BABY).
        e.g.: https://www.uniqlo.com/ca/api/commerce/v3/en/products?limit=1
        """
        json_response = json.loads(response.body_as_unicode())
        status = json_response['status']
        if status == 'ok':
            genders = json_response['result']['aggregations']['tree']['genders']
            for gender in genders:
                uniqlo_item = UniqloItem()
                gender_id = gender['id']
                uniqlo_item['gender_id'] = gender_id
                uniqlo_item['gender_name'] = gender['name']
                url = f'{self.get_gender_url(gender_id)}&limit=1'
                yield scrapy.Request(url, meta={'uniqlo_item': uniqlo_item}, callback=self.parse_gender)

    def parse_gender(self, response):
        """
        Get product level 2 category (e.g., OUTERWEAR).
        e.g.: https://www.uniqlo.com/ca/api/commerce/v3/en/products?path=384&limit=1&offset=0
        """
        uniqlo_item = response.meta['uniqlo_item']
        json_response = json.loads(response.body_as_unicode())
        status = json_response['status']
        if status == 'ok':
            classes = json_response['result']['aggregations']['tree']['classes']
            for class_ in classes:
                class_id = class_['id']
                uniqlo_item['class_id'] = class_id
                uniqlo_item['class_name'] = class_['name']
                url = f'{self.get_class_url(class_id)}&limit=1'
                yield scrapy.Request(url, meta={'uniqlo_item': uniqlo_item}, callback=self.parse_class)

    def parse_class(self, response):
        """
        Get product level 3 category (e.g., Ultra Light Down).
        e.g.: https://www.uniqlo.com/ca/api/commerce/v3/en/products?path=,470&limit=1&offset=0
        """
        uniqlo_item = response.meta['uniqlo_item']
        json_response = json.loads(response.body_as_unicode())
        status = json_response['status']
        if status == 'ok':
            categories = json_response['result']['aggregations']['tree']['categories']
            for category in categories:
                category_id = category['id']
                uniqlo_item['category_id'] = category_id
                uniqlo_item['category_name'] = category['name']
                url = f'{self.get_category_url(category_id)}&limit=1'
                yield scrapy.Request(url, meta={'uniqlo_item': uniqlo_item}, callback=self.parse_category)

    def parse_category(self, response):
        """
        Get product level 4 category (e.g., Vest).
        e.g.: https://www.uniqlo.com/ca/api/commerce/v3/en/products?path=,,471&limit=1&offset=0
        """
        uniqlo_item = response.meta['uniqlo_item']
        json_response = json.loads(response.body_as_unicode())
        status = json_response['status']
        if status == 'ok':
            subcategories = json_response['result']['aggregations']['tree']['subcategories']
            for subcategory in subcategories:
                subcategory_id = subcategory['id']
                uniqlo_item['subcategory_id'] = subcategory_id
                uniqlo_item['subcategory_name'] = subcategory['name']
                url = f'{self.get_subcategory_url(subcategory_id)}&limit=24&offset=0'
                yield scrapy.Request(url, meta={'uniqlo_item': uniqlo_item}, callback=self.parse_subcategory)

    def parse_subcategory(self, response):
        """
        Iterate through products under the subcategory.
        e.g.: https://www.uniqlo.com/ca/api/commerce/v3/en/products?path=,,,472&limit=24&offset=0
        """
        uniqlo_item = response.meta['uniqlo_item']
        json_response = json.loads(response.body_as_unicode())
        status = json_response['status']
        if status == 'ok':
            result = json_response['result']
            offset = result['pagination']['offset']
            items = result['items']
            for item in items:
                product_id = item['productId']
                url = self.get_product_url(product_id)
                yield scrapy.Request(url, meta={'uniqlo_item': uniqlo_item}, callback=self.parse_product)

            next_url = f'{response.url.rsplit("=")[0]}{offset}'
            yield scrapy.Request(next_url, meta={'uniqlo_item': uniqlo_item}, callback=self.parse_subcategory)

    def parse_product(self, response):
        """
        Parse product data then send to pipeline.
        e.g.: https://www.uniqlo.com/ca/api/commerce/v3/en/products/E409114-000
        """
        uniqlo_item = response.meta['uniqlo_item']
        json_response = json.loads(response.body_as_unicode())
        status = json_response['status']
        if status == 'ok':
            item = json_response['result']['items'][0]

            uniqlo_item['care_instruction'] = item['careInstruction']
            uniqlo_item['composition'] = item['composition']
            uniqlo_item['design_detail'] = item['designDetail']
            uniqlo_item['free_information'] = item['freeInformation']
            uniqlo_item['l1_id'] = item['l1Id']
            uniqlo_item['product_id'] = item['productId']
            uniqlo_item['short_description'] = item['shortDescription']
            uniqlo_item['long_description'] = item['longDescription']
            uniqlo_item['name'] = item['name']
            uniqlo_item['size_chart_url'] = item['sizeChartUrl']
            uniqlo_item['size_information'] = item['sizeInformation']
            uniqlo_item['unisex_flag'] = item['unisexFlag']
            uniqlo_item['washing_information'] = item['washingInformation']

            # Product attributes that need further process.
            uniqlo_item['images'] = item['images']
            uniqlo_item['rating'] = item['rating']
            uniqlo_item['commodities'] = item['l2s']
            uniqlo_item['reviews'] = item['reviews']
            yield uniqlo_item
