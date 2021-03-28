# -*- coding: utf-8 -*-
# items.py 用于定义我们爬取的每个实体，例如title，image等

# Define here the models for your scraped items
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ColorMetalItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    change = scrapy.Field()
    date = scrapy.Field()

    pass
