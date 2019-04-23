# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
from spider.db import models


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
                                         subcategory_name=item['subcategory_name'])[0]

    def save_product(self, kind, item):
        product = models.Product.get_or_none(models.Product.id == item['l1_id'])
        if not product:
            product = models.Product.create(id=item['l1_id'],
                                           kind_id=kind,
                                           product_id=item['product_id'],
                                           name=item['name'],
                                           short_description=item['short_description'],
                                           long_description=item['long_description'],
                                           care_instruction=item['care_instruction'],
                                           composition=item['composition'],
                                           design_detail=item['design_detail'],
                                           free_information=item['free_information'],
                                           size_chart_url=item['size_chart_url'],
                                           size_information=item['size_information'],
                                           unisex_flag=int(item['unisex_flag']),
                                           washing_information=item['washing_information'])

        return product
        # rowid = (models.Product.insert(id=item['l1_id'],
        #                                kind_id=kind,
        #                                product_id=item['product_id'],
        #                                name=item['name'],
        #                                short_description=item['short_description'],
        #                                long_description=item['long_description'],
        #                                care_instruction=item['care_instruction'],
        #                                composition=item['composition'],
        #                                design_detail=item['design_detail'],
        #                                free_information=item['free_information'],
        #                                size_chart_url=item['size_chart_url'],
        #                                size_information=item['size_information'],
        #                                unisex_flag=int(item['unisex_flag']),
        #                                washing_information=item['washing_information'],
        #                                updated_at=datetime.datetime.utcnow())
        #          .on_conflict(conflict_target=[models.Product.id],
        #                       preserve=[models.Product.kind_id,
        #                                 models.Product.product_id,
        #                                 models.Product.name,
        #                                 models.Product.short_description,
        #                                 models.Product.long_description,
        #                                 models.Product.care_instruction,
        #                                 models.Product.composition,
        #                                 models.Product.design_detail,
        #                                 models.Product.free_information,
        #                                 models.Product.size_chart_url,
        #                                 models.Product.size_information,
        #                                 models.Product.unisex_flag,
        #                                 models.Product.washing_information,
        #                                 models.Product.updated_at])
        #          .execute())

        # return models.Product.get_by_id(rowid)

    def save_rating(self, product, item):
        rating_obj = item['rating']
        if rating_obj:
            models.Rating.create(product_id=product,
                                 average=float(rating_obj['average']),
                                 fit=float(rating_obj['fit']),
                                 one_count=int(rating_obj['rateCount']['one']),
                                 two_count=int(rating_obj['rateCount']['two']),
                                 three_count=int(rating_obj['rateCount']['three']),
                                 four_count=int(rating_obj['rateCount']['four']),
                                 five_count=int(rating_obj['rateCount']['five']))

    def save_reviews(self, product, item):
        reviews_obj = item['reviews']['items']
        for review_obj in reviews_obj:
            models.Review.get_or_create(product_id=product,
                                        age_range=int(review_obj['ageRange']),
                                        title=review_obj['title'],
                                        comment=review_obj['comment'],
                                        created_at=datetime.datetime.utcfromtimestamp(int(review_obj['createDate'])),
                                        gender_code=review_obj['gender']['code'],
                                        gender_name=review_obj['gender']['name'],
                                        location=review_obj['location'],
                                        name=review_obj['name'],
                                        rate=int(review_obj['rate']),
                                        is_recommend=bool(review_obj['recommendFlag']))

    def save_images(self, product, item):
        images_obj = item['images']
        for image_type, images in images_obj.items():
            for i in images:
                color_display_code = i['colorCode'] if 'colorCode' in i.keys() else ''
                models.Image.get_or_create(product_id=product,
                                           type=image_type,
                                           color_display_code=color_display_code,
                                           url=i['url'])

    def save_commodities(self, product, item):
        for commodity_obj in item['commodities']:
            commodity_flags = []
            color = models.Color.get_or_create(code=commodity_obj['color']['code'],
                                               display_code=commodity_obj['color']['displayCode'],
                                               name=commodity_obj['color']['name'])[0]
            size = models.Size.get_or_create(code=commodity_obj['size']['code'],
                                             display_code=commodity_obj['size']['displayCode'],
                                             name=commodity_obj['size']['name'])[0]
            pld = models.Pld.get_or_create(code=commodity_obj['pld']['code'],
                                           display_code=commodity_obj['pld']['displayCode'],
                                           name=commodity_obj['pld']['name'])[0]

            prices_obj = commodity_obj['prices']
            if prices_obj['base']:
                is_promo = False
                price = float(prices_obj['base']['value'])
                price_currency = prices_obj['base']['currency']['code']
            else:
                is_promo = True
                price = float(prices_obj['promo']['value'])
                price_currency = prices_obj['promo']['currency']['code']

            commodity = models.Commodity.create(commodity_id=commodity_obj['l2Id'],
                                                product_id=product,
                                                communication_code=commodity_obj['communicationCode'],
                                                is_sale=bool(commodity_obj['sales']),
                                                stock_quantity=int(commodity_obj['stock']['quantity']),
                                                color_code=color,
                                                size_code=size,
                                                pld_code=pld,
                                                is_promo=is_promo,
                                                price=price,
                                                price_currency=price_currency)

            flags_obj = commodity_obj['flags']['productFlags'] + commodity_obj['flags']['priceFlags']
            for flag_obj in flags_obj:
                flag = models.Flag.get_or_create(id=int(flag_obj['id']),
                                                 code=flag_obj['code'],
                                                 name=flag_obj['name'])[0]
                models.CommodityFlag.create(commodity_snapshot_id=commodity,
                                            flag_id=flag)
            # with models.db.atomic():
            #     models.CommodityFlag.bulk_create(commodity_flags)
