#!/usr/bin/env python
# encoding: utf-8

import pandas as pd

movies = pd.read_csv('https://blog.searchinfogo.com/download/data/data/imdb_1000.csv')
print(movies.head())
print(movies.shape)

print(type(True))

booleans = []
for length in movies.duration:
    if length >= 20:
        booleans.append(True)
    else:
        booleans.append(False)

booleans[0:5]

len(booleans)

is_long = pd.Series(booleans)
is_long.head()

is_long = movies.duration >= 200
is_long.head()
movies['genre']

movies[movies.duration >= 200]['genre']
movies[is_long]
