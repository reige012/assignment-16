#!/usr/bin/env python
# encoding: utf-8

"""
This function determines the number of weekend days left in 2016 with today
(15 Mar 2016) as the start date and the last day of the year (31 Dec 2016)
as the end date. This is edited from the original to work more effectively with
the unittest module.

Edited by Alicia Reigel. 15 March 2016.
Copyright Alicia Reigel. Louisiana State University. 15 March 2016. All
rights reserved.

"""


import datetime


def format_input_dates(year, month, day):
    new_date = datetime.date(year, month, day)
    print(new_date)
    return new_date


def figure_out_weekends(d1, d2):
    count_weekend_days = 0
    while d2 != d1:
        d2 -= datetime.timedelta(days=1)
        # while date2 is larger than date 1 then subtract a day
        if d2.isoweekday() not in range(1, 6):
            count_weekend_days += 1
        # if that day is not a weekday (1,6) then add it to the count
        # weekends are actually 6 & 7, but range requires me to add the six to get 1-5 inclusive
    return count_weekend_days


def main():
    date1 = format_input_dates(2016, 3, 15)
    date2 = format_input_dates(2016, 12, 31)
    count_of_weekend_days = figure_out_weekends(date1, date2)
    date1_pretty = datetime.date.isoformat(date1)
    date2_pretty = datetime.date.isoformat(date2)
    print("There are {} weekend days between {} and {}.".format(count_of_weekend_days, date1_pretty, date2_pretty))


if __name__ == '__main__':
    main()
