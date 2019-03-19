# -*- coding: utf-8 -*-
import scrapy


class UniqloCaSpider(scrapy.Spider):
    name = 'uniqlo_ca'
    allowed_domains = ['uniqlo.com/ca']
    start_urls = ['http://uniqlo.com/ca/en/']

    def parse(self, response):
        pass
