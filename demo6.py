#!/usr/bin/env python
# encoding: utf-8
import pandas as pd

movies = pd.read_csv('https://blog.searchinfogo.com/download/data/data/imdb_1000.csv')
print(movies.head())

print(movies['title'].sort_values(ascending=False))

print(movies['title'])

print(movies.sort_values('title'))

print(movies.sort_values('duration', ascending=False))

print(movies.head())

print(movies.sort_values(['content_rating', 'duration']))
