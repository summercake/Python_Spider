# -*- coding: utf-8 -*-
import scrapy
import json
from douyuMM.items import DouyummItem


class MmpicSpider(scrapy.Spider):
    name = "MMPic"
    allowed_domains = ["capi.douyucdn.cn"]
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        data = json.loads(response.text)["data"]
        for each in data:
            item = DouyummItem()
            item["nickname"] = each["nickname"]
            item["imageLink"] = each["vertical_src"]
            yield item
        if self.offset < 1000:
            self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
