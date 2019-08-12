#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 内建模块
from datetime import datetime
now = datetime.now()
print(now)

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

# 第三方模块
import requests
r = requests.get('https://www.douban.com/')
print(r.status_code)