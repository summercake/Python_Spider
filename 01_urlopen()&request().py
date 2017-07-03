# coding=utf-8
import urllib2

# 爬虫和反爬虫斗争的第一步
ua_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# 通过urllib2.Request()方法构建一个请求对象
request = urllib2.Request("http://www.jianshu.com", headers=ua_header)
# 向指定的url发送请求, 并返回服务器响应的类文件对象
html = urllib2.urlopen(request)

# 服务器返回的类文件对象支持python文件对象的操作方法
# ready()方法就是读取文件里的全部内容, 并返回字符串
# 打印响应内容
print html.read()

# 获取 HTTP 的响应码
print html.getcode()

# 获取实际数据的 URL, 防止重定向
print html.geturl()

# 获取服务器响应的 HTTP 的包头
print html.info()

print urllib2.urlopen("http://www.baidu.com").read()

'''
# Header
# Host: www.baidu.com
# Connection: keep-alive
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Referer: http://www.baidu.com/
# Accept-Encoding: gzip, deflate, sdch, br
# Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
# Cookie: BAIDUID=04E4001F34EA74AD4601512DD3C41A7B:FG=1; BIDUPSID=04E4001F34EA74AD4601512DD3C41A7B; PSTM=1470329258; MCITY=-343%3A340%3A; BDUSS=nF0MVFiMTVLcUh-Q2MxQ0M3STZGQUZ4N2hBa1FFRkIzUDI3QlBCZjg5cFdOd1pZQVFBQUFBJCQAAAAAAAAAAAEAAADpLvgG0KGyvLrcyfrG-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFaq3ldWqt5XN; H_PS_PSSID=1447_18240_21105_21386_21454_21409_21554; BD_UPN=12314753; sug=3; sugstore=0; ORIGIN=0; bdime=0; H_PS_645EC=7e2ad3QHl181NSPbFbd7PRUCE1LlufzxrcFmwYin0E6b%2BW8bbTMKHZbDP0g; BDSVRTM=0
'''
