# from bs4 import BeautifulSoup
import numpy as np
import pandas as pnd

# import matplotlib.pyplot as plot

df = pnd.read_csv('weatherHistory.csv')

print('simple csv ', df.head)
print('Type Of Date Field ', type(df['Formatted Date'][0]))

df = pnd.read_csv('weatherHistory.csv', parse_dates=['Formatted Date'])

print('date filed formatted csv ', df.head)
print('Type Of Date Field ', type(df['Formatted Date'][0]))

# filled NaN to 0 , inplace=True means it update the df value other with default it will return  a new value
df.fillna(0, inplace=True)

print('First 5 data \n', df.head(5))


print('Last Five data\n', df.tail(5))
print('Print 2 to 5 \n', df[2: 5])
print('columns Name \n', df.columns)
print('columns Type of Summary Field \n', type(df['Summary']))

print('Show Selected Columns\n', df[['Summary', 'Temperature (C)']])

print('All Statistics at a time\n', df.describe())


print('Maximum Temperature\n', df['Temperature (C)'].max())
print('data with max temp ',
      df[df['Temperature (C)'] == df['Temperature (C)'].max()])
print('data with max temp of selected field\n',
      df[['Formatted Date', 'Temperature (C)', 'Summary', 'Precip Type']][df['Temperature (C)'] == df['Temperature (C)'].max()])

print('Min Temperature', df['Temperature (C)'].min())

print('Avarage WindSpeed', df['Wind Speed (km/h)'].mean)

print('Temperature More then 30',
      df['Temperature (C)'][df['Temperature (C)'] > 30])
print('Day which  Rain', df['Formatted Date']
      [df['Summary'] == 'Rain'])

print('Day which Rainy', df['Formatted Date']
      [df['Daily Summary'].str.contains('Rain')])

# changing the index [ first serial number or location]


df.set_index('Precip Type', inplace=True)

print('on location Rain data\n', df.head(5))
print('on location Rain data\n', df.loc['rain'])


# reading data from dictionry or array using DataFrame
wd = {
    'day': ['1/1/2017', '1/2/2017', '1/4/2017', '1/5/2017'],
    'temp': [32, 25, 34, 31],
    'event': ['Rain', 'sunny', 'snow', 'rain']
}

df = pnd.DataFrame(wd)


print('Dataframe from Dictionery\n', df)


# reading data from tuple array using DataFrame and need to pass column nae manually
wd = [
    ('1/1/2017', 34, 'Rain'),
    ('1/2/2017', 32, 'sunny'),
    ('1/4/2017', 25, 'rain')
]

df = pnd.DataFrame(wd)
print('Dataframe from tuple array [Withoout column Name]\n', df)
df = pnd.DataFrame(wd, columns=['day', 'temp', 'event'])
print('Dataframe from tuple array [assign column Name]\n', df)

# column value array [ as like noSQL data]
wd = [
    {'day': '1/1/2017', 'temp': 34, 'event': 'Rain'},
    {'day': '1/2/2017', 'temp': 32, 'event': 'Sunny'},
    {'day': '1/4/2017', 'temp': 25, 'event': 'Cloudy'},
    {'day': '4/4/2017', 'temp': 35, 'event': 'Sunny'}
]


df = pnd.DataFrame(wd)
print('Dataframe from column value array\n', df)


# group by


gsum = df.groupby('event')
for su, s_def in gsum:
    print(su)
   # print(s_def[['Summary', 'Precip Type', 'Temperature (C)',
    #      'Visibility (km)', 'Loud Cover', 'Pressure (millibars)']])
print('Showing group Sunny\n', gsum.get_group('Sunny'))
f = gsum.max()
print('All Max of all group\n', f)


# concat data
wd1 = [
    {'day': '1/4/2017', 'temp': 24, 'event': 'Rain'},
    {'day': '1/2/2017', 'temp': 42, 'event': 'Sunny'},
    {'day': '1/1/2017', 'temp': 25, 'event': 'Cloudy'},
    {'day': '4/4/2017', 'temp': 55, 'event': 'Sunny'}
]
df1 = pnd.DataFrame(wd1)


# add df1 dataset bellow df dataset
df2 = pnd.concat([df, df1])

print('concat df1 to df\n', df2)

df3 = pnd.merge(df, df1, on='event')

print('Merge df1 to df link with event\n', df3)
df2.fillna(0, inplace=True)

# pivote find avarage [ row to column]
print('\n-----------Pvot Avg\n',
      df2.pivot_table(index='event', columns='day', aggfunc='mean'))

# pivote find Max
print('\n---------------Pvot Max\n',
      df2.pivot_table(index='event', columns='day', aggfunc='max'))

# Melt Column to Row
wd1 = [
    {'day': 'Monday', 'Dhaka': 24, 'Citg': 24, 'Syl': 34, 'Rong': 45},
    {'day': 'Tues', 'Dhaka': 23, 'Citg': 21, 'Syl': 35, 'Rong': 35},
    {'day': 'Wed', 'Dhaka': 26, 'Citg': 54, 'Syl': 54, 'Rong': 55},
    {'day': 'Thu', 'Dhaka': 44, 'Citg': 24, 'Syl': 24, 'Rong': 15}
]

df = pnd.DataFrame(wd1)
df1 = pnd.melt(df, id_vars='day', var_name='City', value_name='temp')

print('\n-----------Melt\n', df1)


# stack and unstack
de = pnd.read_excel('stocks.xlsx', header=[0, 1])
print('normal [second row columns] stack\n', de.stack())
df_st = de.stack(level=0)
print('first row as column stack\n', df_st)
print('Unstack\n', df_st.unstack())


# crosstab

df = pnd.read_excel("survey.xlsx")
df1 = pnd.crosstab(df.Nationality, df.Handedness)
print('Crosstab\n', df1)

df1 = pnd.crosstab(df.Sex, df.Handedness)
print('Crosstab\n', df1)

# Crosstab Multi Index Column and Rows
df1 = pnd.crosstab(df.Sex, [df.Handedness, df.Nationality], margins=True)
print('Crosstab Multi Index\n', df1)


df1 = pnd.crosstab([df.Nationality, df.Sex], [df.Handedness], margins=True)
print('Crosstab Multi Index1\n', df1)

# Normalize crosstab
df1 = pnd.crosstab(df.Sex, df.Handedness, normalize='index')
print('Crosstab Normalize\n', df1)

# Aggfunc and Values
df1 = pnd.crosstab(df.Sex, df.Handedness, values=df.Age, aggfunc=np.average)
print('Crosstab aggr age\n', df1)
