#! /usr/bin/env python
# encoding UTF-8

'''
Assignment16Task2 biol7800
ZacCarver 03/30/2016
'''

#import csv
import pandas as pd
import datetime


def num_entries(df):
    l = len(df)
    return l


def date_l(df):
    beg = datetime.datetime.strptime(df['Date'].min(), "%Y-%m-%d")
    return beg


def date_r(df):
    end = datetime.datetime.strptime(df['Date'].max(), "%Y-%m-%d")
    return end


def since(r):
    now = datetime.date.today()
    years = now.year - r.year
    return years


def fltr(df):
    #stackoverflow.com/questions/22394598/select-specific-csv-columns-filtering-python-pandas
    fun_hos = df.iloc[:, (1, 2)]
    return fun_hos


def main():
    df = pd.read_csv('mycosph.csv', parse_dates=[0])
    #d = pd.to_datetime(df['Date'])
    n = num_entries(df)
    print('number of entries: ', n)
    fun_hos = fltr(df)
    print('fungus and its substrate:' '\n', fun_hos)
    l = date_l(df)
    print('collection started: {}-{}-{}'.format(l.month, l.day, l.year))
    r = date_r(df)
    s = since(r)
    print('{} years since last specimen in {}'.format(s, r.year))


if __name__ == '__main__':
    main()
