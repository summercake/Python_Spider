import urllib2
import json
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
request = urllib2.Request(url, headers=header)
response = urllib2.urlopen(request)
html = response.read()
# transform json to python data object
json.loads(html)
unicodestr = json.loads(html)
city_list = jsonpath.jsonpath(unicodestr, "$..name")
for item in city_list:
    print item

array = json.dumps(city_list, ensure_ascii=False)
with open("lagoucity.json", "w") as f:
    f.write(array.encode("utf-8"))
