# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UniqloItem(Item):
    gender_id = Field()          # 384
    gender_name = Field()        # WOMEN
    class_id = Field()           # 470
    class_name = Field()         # OUTERWEAR
    category_id = Field()        # 475
    category_name = Field()      # Ultra Light Down
    subcategory_id = Field()     # 476
    subcategory_name = Field()   # Vest
    product_id = Field()         # E409114-000
    l1_id = Field()              # 409114
    care_instruction = Field()
    composition = Field()
    design_detail = Field()
    free_information = Field()
    short_description = Field()
    long_description = Field()
    name = Field()
    size_chart_url = Field()
    size_information = Field()
    unisex_flag = Field()
    washing_information = Field()

    # Product attributes that need further process
    images = Field()
    rating = Field()
    commodities = Field()
    reviews = Field()

