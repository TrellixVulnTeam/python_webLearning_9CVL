# !/usr/bin/env python
#coding:utf-8

import urllib2

url = "http://www.itcast.cn"

# IE9.0的User-Agent,包含在ua_header里
ua_header = {"User-Agent":"Mozilla/5.0 (compatible;MSIE 9.0; Windows NT 6.1;Trident/5.0;)"}

# url连同headers，一起构造request请求，这个请求将附带IE9.0浏览器的User-Agent
request = urllib2.Request(url,headers=ua_header)

#向服务器发送这个请求
response = urllib2.urlopen(request)

html = response.read()
print html