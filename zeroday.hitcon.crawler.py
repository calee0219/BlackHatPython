#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

url = 'https://zeroday.hitcon.org/vulnerability/disclosed/page/'

for num in range(10):
    res = requests.get(url+str(num))
    soup = BeautifulSoup(res.text, 'html.parser')
    h4 = soup.select('h4.vu-l-data-titl')
    for ll in h4:
        if re.search(u"洩漏", ll.text):
            # print(ll)
            new_url = 'https://zeroday.hitcon.org' + ll.a.get('href')
            new_res = requests.get(new_url)
            new_soup = BeautifulSoup(new_res.text, 'html.parser')
            for msg in new_soup.select('span.stat-tn-stat'):
                if re.search(u'未回報修補狀況', msg.text):
                    print(new_url)
                    break
