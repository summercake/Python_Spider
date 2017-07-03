# coding=utf-8
import urllib

url = "http://www.baidu.com"
wd = {"wd": "传智播客"}

# urlencode() 是对链接内容进行 URL 编码, 该方法接收的是字典
code = urllib.urlencode(wd)
print code

# unquote() 是对链接内容进行反编码
code = urllib.unquote(code)
print code



