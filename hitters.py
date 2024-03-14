import pandas as pd
from os import path

data = pd.read_csv('hitter.csv')
pos = pd.read_csv('razzball.csv')

newdata = data.rename(columns={'PlayerId': 'FangraphsId'})

newdata['Points'] = newdata['1B'] + newdata['2B'] * 2 + newdata['3B'] * 3 + newdata['HR'] * 4 + newdata['R'] + newdata['RBI'] + newdata['BB'] + newdata['HBP'] + newdata['SB'] * 2
newdata['PointAverage'] = newdata['Points'] / newdata['G']
newdata.sort_values('Points', ascending=False, inplace=True)

trimmed = newdata[['Name', 'Team', 'Points', 'PointAverage', 'FangraphsId']]

pos.rename(columns={'FangraphsID': 'FangraphsId', 'ESPN_POS': 'POS'}, inplace=True)

combined = pd.merge(trimmed, pos[['POS', 'FangraphsId']], on='FangraphsId')

combined.to_csv('hitter_points.csv')