# from bs4 import BeautifulSoup
import pandas as pnd
from io import StringIO
# import matplotlib.pyplot as plot

# Pandas read_html() is a function that reads HTML tables into a list of DataFrame objects.
file_path = 'index.html'

# reading File Content
with open(file_path, 'r') as f:
    dhtml = f.read()

# using BeautifulSoup
# soup = BeautifulSoup(dhtml)

# print(soup.prettify())
# dfs = pnd.read_html(StringIO(str(soup)))

dfs = pnd.read_html(StringIO(dhtml))
print(dfs)


# from url
url = 'https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=table_es1a'
dfs = pnd.read_html(url, header=0)
print(dfs[1])

url = 'https://simple.wikipedia.org/wiki/List_of_U.S._states'
dfs = pnd.read_html(url, header=0)
df = pnd.DataFrame(dfs[0])
# write or save the csv
df.to_csv('D:\List_of_U.S_states.csv')
# get columns
print(dfs[0].columns)
# show 1 column data
print(dfs[0]['Flag, name and postal abbreviation [1]'])
