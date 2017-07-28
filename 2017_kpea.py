#!/usr/bin/env python3
from numpy import genfromtxt
import pandas


raw_data=genfromtxt('PrElecData1.csv', delimiter=',')

dataframe=pandas.DataFrame(raw_data)
dfrank=dataframe.rank(axis=0, ascending=True, method='min', na_option='bottom')
print("The Correlations of Raw Data ")
print(dataframe.corr())
print("The Correlations of Ranks")
print(dfrank.corr())
dfmax=dataframe.max(axis=0)
dfmin=dataframe.min(axis=0)
dfgap=(dfmax-dfmin)
dfmul=100/dfgap
dfeql=(dataframe-dfmin)*dfmul
print('Equalised values')
print(dfeql)
print('Equalised values\' variances')
print(dfeql.var(axis=0))
