#!/usr/bin/env python
# encoding: utf-8

import pandas as pd

ufo = pd.read_csv('https://blog.searchinfogo.com/download/data/data/ufo.csv')

head = ufo.head()

print(head)

print(ufo.columns)

ufo.rename(columns={'Colors Reported': 'Colors_Reported', 'Shape Reported': 'Shape_Reported'}, inplace=True)

print(ufo.columns)

ufo_cols = {'city', 'colors reported', 'shape reported', 'state', 'time'}

ufo.columns = ufo_cols

print(ufo.head())

ufo = pd.read_csv('https://blog.searchinfogo.com/download/data/data/ufo.csv', names=ufo_cols, header=0)
print(ufo.head())

print(ufo.columns)

ufo.columns = ufo.columns.str.replace(' ', '_')
print(ufo.columns)
