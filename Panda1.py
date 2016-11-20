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

#summary statistics
df.describe()

#simple plot
df.plot()
df.show()

#return a dataframe showing matrix of correlation
df.corr()



