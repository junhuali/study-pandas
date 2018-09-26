#!/usr/bin/env python
# encoding: utf-8

import pandas as pd

movies = pd.read_csv('https://blog.searchinfogo.com/download/data/data/imdb_1000.csv')
head = movies.head()
print(head)

describe = movies.describe()
print(describe)

shape = movies.shape
print(shape)

dtypes = movies.dtypes
print(dtypes)

print(type(movies))

movies.describe(include=['object'])
