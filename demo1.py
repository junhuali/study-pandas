#!/usr/bin/env python
# encoding: utf-8

import pandas as pd

''' 因为视频中的地址不可用，可以用网盘中的文件，或者用我提供的文件地址'''

orders = pd.read_table('https://blog.searchinfogo.com/download/data/data/chipotle.tsv')

print(orders)

head = orders.head()
print(head)

user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table("https://blog.searchinfogo.com/download/data/data/u.user", sep='|', header=None, names=user_cols)
print(users)
