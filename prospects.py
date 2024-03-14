import pandas as pd
from os import path

prospects = pd.read_csv('theboard_rank.csv')
prospects_merge = prospects[[ 'Name', 'Pos', 'FV', 'ETA', 'Age','Org', 'PlayerId' ]]

intl = pd.read_csv('theboard_intl.csv')
intl_merge = intl[['Name', 'Pos', 'FV', 'ETA', 'Age', 'Proj Team',  'PlayerId']]

draft = pd.read_csv('theboard_college.csv')
draft_merge = draft[['Name', 'Pos', 'FV', 'Age']]


print(intl_merge.head())
print(prospects_merge.head())
print(draft_merge.head())
print(draft.columns)

merge = pd.concat([draft_merge, intl_merge, prospects_merge])
merge.sort_values(['FV', 'ETA'], inplace=True, ascending=[False, True])
print(merge.head(40))
merge.to_csv('prospects.csv')