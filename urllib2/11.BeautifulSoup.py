from bs4 import BeautifulSoup
import requests
import time


def captcha(captcha_data):
    with open("captcha.jpg", "wb") as f:
        f.write(captcha_data)
    text = raw_input("Plz input verify code")
    return text


def zhihuLogin():
    # create a Session object
    sess = requests.Session()
    # this is request header
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    # get login page first, next, find POST data, next, get current login page cookie
    html = sess.get("https://www.zhihu.com/#signin", headers=header).text
    # use lxml
    bs = BeautifulSoup(html, "lxml")
    # get login page _xsrf value
    # the role of _xsrf is that it can prevent Cross-Site Request Forgery
    # Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they're currently authenticated.
    # use MD5 string to inspect user's Cookie and Session
    _xsrf = bs.find("input", attrs={"name": "_xsrf"}).get("value")
    captcha_url = "https://www.zhihu.com/captcha.gif?r=%d&type=login" % (time.time() * 1000)
    captcha = sess.get(captcha_url, headers=header).content
    data = {
        "_xsrf": _xsrf,
        "email": "123636274@qq.com",
        "password": "ALARMCHIME",
        "captcha": text
    }
    response = sess.get("https://www.zhihu.com/people/maozhaojun/activities", headers = header)
    with open("my.html", "w") as f:
        f.write(response.text.encode("utf-8"))

if __name__ == "__main__":
    zhihuLogin()
