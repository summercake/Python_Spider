# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItems(scrapy.Item):
    # name
    name = scrapy.Field()
    # position
    title = scrapy.Field()
    # brief
    info = scrapy.Field()
