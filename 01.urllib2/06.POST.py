# coding=utf-8
import urllib
import urllib2

# 通过抓包的方式获取的url，并不是浏览器上显示的url
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

# 完整的headers
header = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}

# 用户接口输入
key = raw_input("Please input the word:")

# 发送到web服务器的表单数据
formdata = {
    "type": "AUTO",
    "i": key,
    "doctype": "json",
    "xmlVersion": "1.8",
    "keyfrom": "fanyi.web",
    "ue": "UTF-8",
    "action": "FY_BY_CLICKBUTTON",
    "typoResult": "true"
}

data = urllib.urlencode(formdata)
request = urllib2.Request(url, data=data, headers=header)
print urllib2.urlopen(request).read()
