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
    db.create_tables([Color, Size, Pld, Kind, Product, ProductImage, Review, Rating, Commodity])


class BaseModel(Model):
    class Meta:
        database = db
        legacy_table_names = False


class Color(BaseModel):
    code = CharField(primary_key=True)
    name = CharField()


class Size(BaseModel):
    code = CharField(primary_key=True)
    name = CharField()


class Pld(BaseModel):
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
    inserted_at = DateTimeTZField(default=datetime.datetime.utcnow())


class ProductImage(BaseModel):
    pass


class Rating(BaseModel):
    pass


class Review(BaseModel):
    pass


class Commodity(BaseModel):
    pass





