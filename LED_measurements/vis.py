#%%

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# read back.txt to pandas dataframe
def read_dataframe(frame):
	data = pd.read_csv(frame, sep='\t', header=None, skiprows=15)
	data.columns = ['x', 'y']
	return data
 
back = read_dataframe('back.txt')
meas1 = read_dataframe('meas1.txt')
 
# plot dataframe
def plot_dataframe(frame):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(frame['x'], frame['y'], c='r', marker='o')
	plt.show()
 
plot_dataframe(back)
plot_dataframe(meas1)
 
 
# %%
