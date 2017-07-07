import urllib2
from lxml import etree
import json

url = "http://www.qiushibaike.com/8hr/page/2/"
header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

request = urllib2.Request(url, headers=header)
html = urllib2.urlopen(request).read()
text = etree.HTML(html)
node_list = text.xpath('//div[contains(@id, "qiushi_tag")]')
items = {}
for item in node_list:
    username = item.xpath('./div/a/@title')[0]
    image = item.xpath('.//div[@class="thumb"]//@src')
    content = item.xpath('.//div[@class="content"]/span')[0].text
    zan = item.xpath('.//i')[0].text
    comments = item.xpath('.//i')[1].text
    items = {
        "username": username,
        "image": image,
        "content": content,
        "zan": zan,
        "comments": comments
    }
    with open("qiushi.json", "a") as f:
        f.write(json.dumps(items, ensure_ascii=False).encode("utf-8")+"\n")
