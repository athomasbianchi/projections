import pandas as pd
from os import path

data = pd.read_csv('hitter.csv')

newdata = data.set_index('PlayerId')
newdata['Points'] = newdata['1B'] + newdata['2B'] * 2 + newdata['3B'] * 3 + newdata['HR'] * 4 + newdata['R'] + newdata['RBI'] + newdata['BB'] + newdata['HBP'] + newdata['SB'] * 2
newdata['PointAverage'] = newdata['Points'] / newdata['G']
newdata.sort_values('Points', ascending=False, inplace=True)

trimmed = newdata[['Name', 'Team', 'Points', 'PointAverage']]
trimmed.to_csv('hitter_points.csv')