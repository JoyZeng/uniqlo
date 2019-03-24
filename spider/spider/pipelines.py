# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
from spider.spider.db import models


class CommodityPipeline(object):
    def __init__(self):
        models.create_tables_if_needed()

    def process_item(self, item, spider):
        kind = self.save_kind(item)
        product = self.save_product(kind, item)
        self.save_rating(product, item)
        self.save_reviews(product, item)
        self.save_images(product, item)
        self.save_commodities(product, item)

        return item

    def save_kind(self, item):
        return models.Kind.get_or_create(gender_id=item['gender_id'],
                                         gender_name=item['gender_name'],
                                         class_id=item['class_id'],
                                         class_name=item['class_name'],
                                         category_id=item['category_id'],
                                         category_name=item['category_name'],
                                         subcategory_id=item['subcategory_id'],
                                         subcategory_name=item['subcategory_name'])

    def save_product(self, kind, item):
        product = models.Product.get_or_create(id=item['l1_id'])
        product.product_id = item['product_id']
        product.name = item['name']
        product.short_description = item['short_description']
        product.long_description = item['long_description']
        product.care_instruction = item['care_instruction']
        product.composition = item['composition']
        product.design_detail = item['design_detail']
        product.free_information = item['free_information']
        product.size_char_url = item['size_char_url']
        product.size_information = item['size_information']
        product.unisex_flag = int(item['unisex_flag'])
        product.washing_information = item['washing_information']
        product.kind_id = kind
        product.updated_at = datetime.datetime.utcnow()
        product.save()
        return product

    def save_rating(self, product, item):
        rating_obj = item['rating']
        if not rating_obj:
            models.Rating.create(product_id=product,
                                 average=float(rating_obj['average']),
                                 fit=float(rating_obj['fit']),
                                 one_count=int(rating_obj['rateCount']['one']),
                                 two_count=int(rating_obj['rateCount']['two']),
                                 three_count=int(rating_obj['rateCount']['three']),
                                 four_count=int(rating_obj['rateCount']['four']),
                                 five_count=int(rating_obj['rateCount']['five']), )

    def save_reviews(self, product, item):
        reviews_obj = item['reviews']['items']
        for review_obj in reviews_obj:
            models.Review.get_or_create(product_id=product,
                                        age_range=int(review_obj['ageRange']),
                                        title=review_obj['title'],
                                        comment=review_obj['comment'],
                                        created_at=datetime.datetime.utcfromtimestamp(int(review_obj['createdDate'])),
                                        gender_code=review_obj['gender']['code'],
                                        gender_name=review_obj['gender']['name'],
                                        location=review_obj['location'],
                                        name=review_obj['name'],
                                        rate=int(review_obj['rate']),
                                        is_recommend=bool(review_obj['recommendFlag']))

    def save_images(self, product, item):
        images_obj = item['images']
        for image_obj in images_obj:
            for image_type, images in image_obj.items():
                for i in images:
                    models.Image.get_or_create(product_id=product,
                                               type=image_type,
                                               color_display_code=i['colorCode'],
                                               url=i['url'])

    def save_commodities(self, product, item):
        for commodity in item['commodities']:
            pass

