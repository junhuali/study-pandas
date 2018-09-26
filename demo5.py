#!/usr/bin/env python
# encoding: utf-8
import pandas as pd

ufo = pd.read_csv('https://blog.searchinfogo.com/download/data/data/ufo.csv')
print(ufo.head())
print(ufo.shape)

# axis=0 按行 axi=1 按列
ufo.drop('Colors Reported', axis=1, inplace=True)
print(ufo.head())

ufo.drop(['City', 'State'], axis=1, inplace=True)
print(ufo.head())

ufo.drop([0, 1], axis=0, inplace=True)
print(ufo.head())
print(ufo.shape)
