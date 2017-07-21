#!/usr/bin/env python3
from numpy import genfromtxt
import pandas

raw_data=genfromtxt('PrElecData1.csv', delimiter=',')

for row in raw_data:
	print(', '+str(row))

dataframe=pandas.DataFrame(raw_data)
#print(dataframe.reindex_axis(labels=['문재인', '홍준표','안철수','유승민','심상정'], axis='columns', copy=True ))
print(dataframe)
#print(dataframe1)
dfrank=dataframe.rank(axis=0, ascending=True, method='min', na_option='bottom')
#rank.reindex(columns=['문재인', '홍준표','안철수','유승민','심상정'] )
print(dfrank)
print("The Correlations of Raw Data ")
print(dataframe.corr())
print("The Correlations of Ranks")
print(dfrank.corr())
