import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table('C:\Git\PandaPlay\BurringtonCombeRide_tcx.txt', sep='\t')

df.info()

df.describe()