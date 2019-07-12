import pandas as pd
import numpy as np

data = pd.read_csv('data/prepocessed.csv', encoding='utf8', engine='python')
data = data.drop(data.columns[0], axis=1)
data = data.loc[data['State'] == 'Wyoming']

data.to_csv('data/Wyoming.csv', ',', encoding='utf8')

dataWyoming = pd.read_csv('data/Wyoming.csv')
dataWyoming = data.groupby(['Date Local', 'County Code']).mean().reset_index()
WyomingCO = dataWyoming[['Date Local', 'CO Mean']].copy()
WyomingCO.to_csv('data/WyomingCO.csv', ',', encoding='utf8')

