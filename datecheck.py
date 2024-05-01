
import calendar
import pandas.tseries.holiday as h
import datetime
from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday
import numpy as np
import pandas as pnd
import matplotlib.pyplot as plt
from pandas.tseries.offsets import CustomBusinessDay

# import matplotlib.pyplot as plot

df = pnd.read_csv('APPL_Stock.csv')

print('simple csv ', df.head)
print('Type Of Date Field ', type(df['Date'][0]))

df = pnd.read_csv('APPL_Stock.csv', parse_dates=['Date'])

print('date filed formatted csv ', df.head)
print('Type Of Date Field ', type(df['Date'][0]))

df = pnd.read_csv('APPL_Stock.csv', parse_dates=['Date'], index_col='Date')

print('Price on 26th Apr 2024  \n', df.loc['2024-04-26'])
print('Price on Jan 2024  \n', df.loc['2024-01'])

print('-Data from 2 feb to 26 feb  ',
      df.sort_index().loc['2024-02-2':'2024-02-26'])
# resample

# B         business day frequency
# C         custom business day frequency (experimental)
# D         calendar day frequency
# W         weekly frequency
# M         month end frequency
# SM        semi-month end frequency (15th and end of month)
# BM        business month end frequency
# CBM       custom business month end frequency
# MS        month start frequency
# SMS       semi-month start frequency (1st and 15th)
# BMS       business month start frequency
# CBMS      custom business month start frequency
# Q         quarter end frequency
# BQ        business quarter endfrequency
# QS        quarter start frequency
# BQS       business quarter start frequency
# A         year end frequency
# BA, BY    business year end frequency
# AS, YS    year start frequency
# BAS, BYS  business year start frequency
# BH        business hour frequency
# H         hourly frequency
# T, min    minutely frequency
# S         secondly frequency
# L, ms     milliseconds
# U, us     microseconds
# N         nanoseconds

print('----Weekly Frequency(mean/avg) of Closing Price \n ',
      df.Close.resample('W').mean())
# plotting
print('----Monthly Frequency(mean/avg) of Closing Price \n ',
      df.Close.resample('ME').mean().plot())
plt.show()

rng = pnd.date_range(start='2024-02-1', end='2024-02-28', freq='B')
print('---date range data from panda\n',
      rng)

# filling missing day data with previous day /// you can see that in this data 3 4 10 11  th feb is missing
# so filling the date with frequency 1 day
df1 = df.asfreq('D', method='pad')

print('-Data from 1 feb to 28 feb  with missing dates from next valid date\n',
      df1.sort_index().loc['2024-02-2':'2024-02-28'])
df1 = df.asfreq('D', method='backfill')

print('-Data from 1 feb to 28 feb  with missing dates from last valid date\n',
      df1.sort_index().loc['2024-02-2':'2024-02-28'])

bzday = CustomBusinessDay(weekmask='Sun Mon Tue Wed Thu')

rng = pnd.date_range(start='2024-03-1', end='2024-03-30', freq=bzday)
print('---date range with Bangaldeshi Business day\n',
      rng)


class bdHolidayCalendar(AbstractHolidayCalendar):

    rules = [

        # USMartinLutherKingJr,
        # USPresidentsDay,
        # USMemorialDay,
        Holiday(
            "Fathers day",
            month=3,
            day=17,
            start_date="2021-03-17",
            observance=nearest_workday,
        ),


        # eid ul fitr
        *[h.Holiday(f'Mar {d}', month=3, day=d) for d in range(10, 13)],
        Holiday("Independence Day", month=3,
                day=26, observance=nearest_workday),
        Holiday("Christmas Day", month=12, day=25, observance=nearest_workday)
    ]


bdh = CustomBusinessDay(calendar=bdHolidayCalendar())

rng = pnd.date_range(start='2024-03-1', end='2024-03-30', freq=bdh)
print('---date range with Bangaldeshi holiday\n',
      rng)
# print([h.Holiday(f'Mar {d}', month=3, day=d) for d in range(10, 13)])


datas = ['2017-01-05', 'Jan 5, 2017', '01/05/2017',
         '2017.01.05', '2017/01/05', '20170105']
# error
print('To Date\n', pnd.to_datetime(datas, format='mixed'))
print('To Date\n', pnd.to_datetime('01/05/2017', dayfirst=False, format='mixed'))

# get last date of a month
m = pnd.Period('2024-4', freq='M')
print('Last Date Of April', m.end_time)

m = m-10
print('10 month  before april ',
      calendar.month_name[m.month],  m.end_time)
