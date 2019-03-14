import numpy as np 
import pandas as pd 
import sqlite3
import matplotlib
matplotlib.use('GTKAgg')
import matplotlib.pyplot as plt
from sklearn import linear_model


def lin_regression(x, y):
	'''
	Makes a linear regression between x and y
	'''

	data, shape = clean_data(x, y)

	reg = linear_model.LinearRegression()

	reg.fit(data, shape)

	hat_vals = reg.predict(data)

	r_sq = reg.score(hat_vals, data)

	plot = plt.plot(data, hat_vals, color='red',linewidth=2)

	return(reg.coef_, r_sq, plot)





def clean_data(x, y):
	'''
	Prepares x and y so that they are usable in a linear regression
	'''

