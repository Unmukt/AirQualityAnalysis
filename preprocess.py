import pandas as pd
import numpy as np


data = pd.read_csv('data/pollution_us_2000_2016.csv', encoding='utf8', engine='python')
data = data.drop(data.columns[0], axis=1)
data = data.fillna(data.groupby(['Date Local', 'County Code']).transform('mean'))

data.to_csv('data/prepocessed.csv', ',', encoding='utf8')

print (data.head)
