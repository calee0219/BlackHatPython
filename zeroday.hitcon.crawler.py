#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

url = 'https://zeroday.hitcon.org/vulnerability/disclosed/page/'

for num in range(10):                               # 想連續 10 頁的資料
    res = requests.get(url+str(num))
    soup = BeautifulSoup(res.text, 'html.parser')   # 將頁數接到 url 後面
    h4 = soup.select('h4.vu-l-data-titl')           # 尋找標題 (裡面包含了連結)
    for ll in h4:
        if re.search(u"洩漏", ll.text):              # 做字串比對，可以把 洩漏 改成想找的關鍵字，ex. XSS, SQL...
            new_url = 'https://zeroday.hitcon.org' + ll.a.get('href')
            new_res = requests.get(new_url)         # 進入新網址
            new_soup = BeautifulSoup(new_res.text, 'html.parser')
            for msg in new_soup.select('span.stat-tn-stat'):
                if re.search(u'未回報修補狀況', msg.text): # 再次字串比對
                    print(new_url)
                    break
