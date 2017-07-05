# coding=utf-8
import urllib
import urllib2


# 读取 html 页面
def load_page(url, filename):
    print "downloading" + filename
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}
    request = urllib2.Request(url, headers=header)
    return urllib2.urlopen(request).read()


# 将 html 内容写入本地
def write_page(html, filename):
    print "saving" + filename
    # 文件写入
    with open(filename, "w") as f:
        f.write(html)
    print "-" * 30


# 爬虫调度器, 负责组合处理每个页面的url
def spider(url, beginPage, endPage):
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        html = load_page(fullurl, filename)
        # print html
        write_page(html, filename)
        print "Thanks!!!"


if __name__ == "__main__":
    kw = raw_input("请输入需要爬取的贴吧名: ")
    beginPage = int(raw_input("请输入起始页: "))
    endPage = int(raw_input("请输入结束页: "))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    spider(fullurl, beginPage, endPage)




