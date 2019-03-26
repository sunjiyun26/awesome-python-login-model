# 这里需要使用getpass模块才能使输入密码不可见
import getpass
import requests
import hashlib
import time

"""
info:
author:CriseLYJ
github:https://github.com/CriseLYJ/
update_time:2019-3-7
"""
from http.cookiejar import CookieJar, LWPCookieJar
from urllib.request import Request, urlopen, HTTPCookieProcessor, build_opener
import urllib.request, urllib.parse, urllib.error
# import http.cookiejar


def get_login(phone, pwd):
    new_time = str(int(time.time()))
    sign = new_time + '_' + hashlib.md5((phone + pwd + new_time).encode("utf-8")).hexdigest()

    print(sign)
    url = "https://appblog.sina.com.cn/api/passport/v3_1/login.php"
    data = {
        "cookie_format": "1",
        "sign": sign,
        "pin": "e3eb41c951f264a6daa16b6e4367e829",
        "appver": "5.3.2",
        "appkey": "2546563246",
        "phone": phone,
        "entry": "app_blog",
        "pwd": pwd
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; nxt-al10 Build/LYZ28N) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 sinablog-android/5.3.2 (Android 5.1.1; zh_CN; huawei nxt-al10/nxt-al10)",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
    }
    session_ = requests.session()
    r = requests.post(url=url, data=data, headers=headers)

    # coget = requests.get('https://m.weibo.cn/').cookies.get_dict()
    # print(coget)
    jar = requests.cookies.RequestsCookieJar()
    # _gookie = r.json()['data']['cookie']
    # for (k,v) in _gookie.items():
    #     jar.set(k,v)
        # jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
        # url = 'https://httpbin.org/cookies'
        # r = requests.get(url, cookies=jar)


    r = requests.get('https://m.weibo.cn/', cookies=jar,headers=headers)
    print(r.text)
    # print(r.json()['data']['cookie'])
    # save_cookie()

def save_cookie():
    filename = 'neihan.txt'
    # 设置cookie保存的文件
    cookie_obj = LWPCookieJar(filename=filename)
    # 创建一个支持cookie的对象，对象属于HTTPCookieProcessor
    cookie_handler = HTTPCookieProcessor(cookie_obj)
    # 创建一个opener
    opener = build_opener(cookie_handler)
    # 请求网页
    response = opener.open('https://m.weibo.cn/')
    # 保存cookie到指定的文件当中去
    # ignore_expires=True 即便目标cookie已经在文件中存在，仍然对其写入
    # ignore_discard=True  即便cookie将要/已经过期，仍然写入
    cookie_obj.save(ignore_expires=True, ignore_discard=True)

if __name__ == '__main__':
    phone = input("你输入你的账号:")
    # 这里输入密码不可见
    pwd = getpass.getpass("password:")

    get_login(phone, pwd)
