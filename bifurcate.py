import pandas as pd
import numpy as np

data = pd.read_csv('prepocessed.csv', encoding='utf8', engine='python')
data = data.drop(data.columns[0], axis=1)
data = data.loc[data['State'] == 'Arizona']

data.to_csv('data/Arizona.csv', ',', encoding='utf8')

dataArizona = pd.read_csv('data/Arizona.csv')
dataArizona = data.groupby(['Date Local', 'County Code']).mean().reset_index()

dataArizona.to_csv('data/ArizonaGrouped.csv', ',', encoding='utf8')

dataCounty13 = dataArizona.loc[dataArizona['County Code'] == 13]
dataCounty19 = dataArizona.loc[dataArizona['County Code'] == 19]

dataCounty13.to_csv('data/ArizonaCounty13.csv', ',', encoding='utf8')
dataCounty19.to_csv('data/ArizonaCounty19.csv', ',', encoding='utf8')

dataCounty19 = pd.read_csv('data/ArizonaCounty19.csv')
data19NO2 = dataCounty19[['Date Local', 'NO2 Mean']].copy()

data19NO2.to_csv('data/Arizona19NO2.csv', ',', encoding='utf8')