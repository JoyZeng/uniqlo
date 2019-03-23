#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng

from .models import *


def create_tables():
    db.connect()
    db.create_tables([], safe=True)



