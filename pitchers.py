import pandas as pd
from os import path

data = pd.read_csv('pitcher.csv')
pos = pd.read_csv('pitcher_pos.csv')

# newdata = data.set_index('PlayerId')
newdata = data
newdata['Points'] = newdata['IP'] * 2 - newdata['H'] / 2 - newdata['ER'] - newdata['BB'] / 2 - newdata['HBP'] / 2 + newdata['SO'] + newdata['W'] * 10 + newdata['SV'] * 5
newdata['PointAverage'] = newdata['Points'] / newdata['G']
newdata.sort_values('Points', ascending=False, inplace=True)

trimmed = newdata[['Name', 'Team', 'Points', 'PointAverage', 'PlayerId']]

combined = pd.merge(trimmed, pos[['POS', 'ADP', 'PlayerId']], on='PlayerId')
print(combined.head())
trimmed.to_csv('pitcher_points.csv')