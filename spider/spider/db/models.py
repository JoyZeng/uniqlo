#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng

import datetime
from playhouse.postgres_ext import *
import config

db = PostgresqlExtDatabase(database=config.DB_NAME,
                           user=config.DB_USER,
                           password=config.DB_PASSWORD,
                           host=config.DB_HOST,
                           port=config.DB_PORT)


def create_tables_if_needed():
    db.connect()
    db.create_tables([Color, Size, Pld, Flag, Kind, Product, ProductImage, Review, Rating, Commodity])


class BaseModel(Model):
    class Meta:
        database = db
        legacy_table_names = False


class Color(BaseModel):
    code = CharField(primary_key=True)
    display_code = CharField()
    name = CharField()


class Size(BaseModel):
    code = CharField(primary_key=True)
    display_code = CharField()
    name = CharField()


class Pld(BaseModel):
    code = CharField(primary_key=True)
    display_code = CharField()
    name = CharField()


class Flag(BaseModel):
    code = CharField(primary_key=True)
    name = CharField()


class Kind(BaseModel):
    id = AutoField()
    gender_id = IntegerField()
    class_id = IntegerField()
    category_id = IntegerField()
    subcategory_id = IntegerField()
    gender_name = CharField()
    class_name = CharField()
    category_name = CharField()
    subcategory_name = CharField()


class Product(BaseModel):
    id = CharField(primary_key=True)
    kind_id = ForeignKeyField(Kind, backref='products')
    product_id = CharField()
    inserted_at = DateTimeTZField(default=datetime.datetime.utcnow())
    updated_at = DateTimeTZField(default=datetime.datetime.utcnow())
    name = CharField()
    short_description = TextField()
    long_description = TextField()
    care_instruction = TextField()
    composition = TextField()
    design_detail = TextField()
    free_information = TextField()
    size_char_url = CharField()
    size_information = TextField()
    unisex_flag = IntegerField()
    washing_information = TextField()


class Image(BaseModel):
    product_id = ForeignKeyField(Product, backref='images')
    color_display_code = CharField()
    type = CharField()
    url = CharField()


class Rating(BaseModel):
    product_id = ForeignKeyField(Product, backref='ratings')
    inserted_at = DateTimeTZField(default=datetime.datetime.utcnow())
    average = FloatField()
    fit = FloatField()
    one_count = IntegerField()
    two_count = IntegerField()
    three_count = IntegerField()
    four_count = IntegerField()
    five_count = IntegerField()


class Review(BaseModel):
    product_id = ForeignKeyField(Product, backref='reviews')
    age_range = IntegerField()
    title = TextField()
    comment = TextField()
    created_at = DateTimeTZField()
    gender_code = IntegerField()
    gender_name = CharField()
    location = CharField()
    name = CharField()
    rate = IntegerField()
    is_recommend = BooleanField()


class Commodity(BaseModel):
    id = CharField(primary_key=True)
    product_id = ForeignKeyField(Product, backref='commodities')
    color_code = ForeignKeyField(Color, backref='commodities')
    size_code = ForeignKeyField(Size, backref='commodities')
    pld_code = ForeignKeyField(Pld, backref='commodities')
    inserted_at = DateTimeTZField(default=datetime.datetime.utcnow())
    communication_code = CharField()
    stock_quantity = IntegerField()
    is_sale = BooleanField()
    price = FloatField()
    price_currency = CharField()
    is_promo = BooleanField()
    flags = ArrayField(CharField)

    class Meta:
        indexes = (
            (('product_id', 'color_code', 'size_code', 'pld_code'), True),
        )



