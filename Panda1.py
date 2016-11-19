import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table('C:\Git\PandaPlay\BurringtonCombeRide_tcx.txt', sep='\t')

#summary pf dataframe
df.info()

#summary statistics
df.describe()

#return a dataframe showing matrix of correlation
df.corr()



