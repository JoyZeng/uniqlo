#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng

from peewee import *
import config

db = PostgresqlDatabase(database=config.DB_NAME,
                        user=config.DB_USER,
                        password=config.DB_PASSWORD,
                        host=config.DB_HOST,
                        port=config.DB_PORT)


class BaseModel(Model):
    class Meta:
        database = db


class Product(BaseModel):
    pass


class Kind(BaseModel):
    pass


class Commodity(BaseModel):
    pass


class Color(BaseModel):
    pass


class Size(BaseModel):
    pass


class Pld(BaseModel):
    pass


class ProductImage(BaseModel):
    pass


class Rating(BaseModel):
    pass


class Review(BaseModel):
    pass
