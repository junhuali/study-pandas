#!/usr/bin/env python
# encoding: utf-8

import pandas as pd

ufo = pd.read_csv('https://blog.searchinfogo.com/download/data/data/ufo.csv')

type = type(ufo)

print(type)

ufo.head()

type(ufo['City'])

print(ufo['City'])

ufo.shape

ufo.City + ufo.State

ufo['Location'] = ufo.City + ',' + ufo.State

print(ufo['Location'])
