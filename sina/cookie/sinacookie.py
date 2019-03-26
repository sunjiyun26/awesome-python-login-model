#!/usr/bin/env python
# -*- coding: utf-8 -*-
from http.cookiejar import CookieJar, LWPCookieJar
from urllib.request import Request, urlopen, HTTPCookieProcessor, build_opener

filename = 'sinacookie.txt'
# 设置cookie保存的文件
cookie_obj = LWPCookieJar(filename=filename)
# 创建一个支持cookie的对象，对象属于HTTPCookieProcessor
cookie_handler = HTTPCookieProcessor(cookie_obj)
# 创建一个opener
opener = build_opener(cookie_handler)
# 请求网页
response = opener.open('http://www.neihanshequ.com')
# 保存cookie到指定的文件当中去
# ignore_expires=True 即便目标cookie已经在文件中存在，仍然对其写入
# ignore_discard=True   即便cookie将要/已经过期，仍然写入
cookie_obj.save(ignore_expires=True, ignore_discard=True)

 