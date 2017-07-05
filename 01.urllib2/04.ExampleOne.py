# coding=utf-8
import urllib
import urllib2

url = "http://www.jianshu.com"

keyword = raw_input("请输入要查询的字符串: ")
wd = {"wd": keyword}
wd = urllib.urlencode(wd)
fullurl = url + "?" + wd
header = {"User-Agent": "Mozilla..."}
request = urllib2.Request(fullurl, headers=header)
response = urllib2.urlopen(request)
print response.read()



