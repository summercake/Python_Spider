import scrapy
from mySpider.items import ItcastItems


# Spider Class
class ItcastSpider(scrapy.Spider):
    # Spider Name
    name = "itcast"
    # Allowed url Range
    allowed_domain = ["http://www.itcast.cn/"]
    # where to start
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]

    def parse(self, response):
        # with open("teacher.html", "w") as f:
        #     f.write(response.body)
        # use scrapy default xpath tool to match all data node
        teacher_list = response.xpath('//div[@class="li_txt"]')
        teacherItem = []
        for each in teacher_list:
            item = ItcastItems()
            # name
            # extract can transform data to UNICODE
            name = each.xpath('./h3/text()').extract()
            # title
            title = each.xpath('./h4/text()').extract()
            # info
            info = each.xpath('./p/text()').extract()
            # print name[0]
            # print title[0]
            # print info[0]
            item['name'] = name[0].encode("gbk")
            item['title'] = title[0].encode("gbk")
            item['info'] = info[0].gbk("gbk")
            teacherItem.append(item)
        return teacherItem
