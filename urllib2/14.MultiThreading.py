# coding=utf-8
import threading
from Queue import Queue
from lxml import etree
import requests
import time
import json


class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        # threading.Thread.__init__(self)
        super(ThreadCrawl, self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    def run(self):
        while not CRAWL_EXIT:
            try:
                page = self.pageQueue.get(False)
                url = "http://www.qiushibaike.com/8hr/" + str(page) + "/"
                content = requests.get(url, headers=self.header)
                time.sleep(1)
                self.dataQueue.put(content)
            except:
                pass
        print "End" + self.threadName


class ThreadParse(threading.Thread):
    def __init__(self, threadName, dataQueue, filename, lock):
        super(ThreadParse, self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        self.filename = filename
        self.lock = lock

    def run(self):
        print "start" + self.threadName
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                self.parse(html)
            except:
                pass
        print "exit" + self.threadName

    def parse(self, html):
        # 解析为HTML DOM
        html = etree.HTML(html)

        node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')

        for node in node_list:
            # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
            username = node.xpath('./div/a/@title')[0]
            # 图片连接
            image = node.xpath('.//div[@class="thumb"]//@src')#[0]
            # 取出标签下的内容,段子内容
            content = node.xpath('.//div[@class="content"]/span')[0].text
            # 取出标签里包含的内容，点赞
            zan = node.xpath('.//i')[0].text
            # 评论
            comments = node.xpath('.//i')[1].text

            items = {
                "username" : username,
                "image" : image,
                "content" : content,
                "zan" : zan,
                "comments" : comments
            }

            # with 后面有两个必须执行的操作：__enter__ 和 _exit__
            # 不管里面的操作结果如何，都会执行打开、关闭
            # 打开锁、处理内容、释放锁
            with self.lock:
                # 写入存储的解析后的数据
                self.filename.write(json.dumps(items, ensure_ascii = False).encode("utf-8") + "\n")


CRAWL_EXIT = False
PARSE_EXIT = False


def main():
    # This queue can contains 10 page
    pageQueue = Queue(10)
    for i in range(1, 11):
        pageQueue.put(i)
    dataQueue = Queue()
    crawl_list = [1, 2, 3]
    threadcrawl = []
    for threadName in crawl_list:
        thread = ThreadCrawl(threadName, pageQueue, dataQueue)
        thread.start()
        threadcrawl.append(thread)
    while not pageQueue.empty():
        pass
    global CRAWL_EXIT
    CRAWL_EXIT = False


if __name__ == "__main__":
    main()
