# -*- coding: utf-8 -*-
import scrapy
from tencentProject.items import TencentprojectItem


class JobPositionSpider(scrapy.Spider):
    name = "Job_Position"
    allowed_domains = ["tencent.com"]
    url = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            item = TencentprojectItem()
            item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['positionLink'] = each.xpath("./td[1]/a/@href").extract()[0]
            # if each.xpath("./td[2]/text()").extract()[0] != "":
            #     item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            # else:
            #     item['positionType'] = "None"
            # item['positionType'] = str(each.xpath("./td[2]/text()").extract()[0])
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            item['pulishTime'] = each.xpath("./td[5]/text()").extract()[0]
            # deliver data to pipe file
            yield item
        if self.offset < 1470:
            self.offset += 10
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
