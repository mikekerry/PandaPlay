import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.parser import parse

df = pd.read_table('C:\Git\PandaPlay\BurringtonCombeRide_tcx.txt', sep='\t')

#summary pf dataframe
df.info()

#convert time column to datetime
df['time'] = pd.to_datetime(df['time'])

#view first 5 and last 5 values
df.head()
df.tail()

#counts of distinct values
df['type'].value_counts()

#return cell
df['time'][0]

#replace nulls
df['name'].fillna('No value',inplace=True)
df['desc'].fillna('No value',inplace=True)

#summary statistics
df.describe()

#plot all
df.plot()

#choose axis
df.plot(x='time', y='altitude (m)')

#next line not required if started ipython in pylab mode (ipython --pylab)
df.show()

#return a dataframe showing matrix of correlation
df.corr()



