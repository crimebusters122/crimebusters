import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.api as sm
from bokesh.plotting import figure, save



def linear_regression(x,y):
	'''
	Makes a linear regression table
	'''

	model = sm.OLS(y, x).fit()

	return model.summary()



def map_of_chicago_crime(c_type = every, year_min = 2001, year_max = 2018,\
	arrest = irrelelevant):
	'''
	Makes a map of the density of a crime in Chicago.  Clicking on a dot/
	    neighborhood will give you more indepth information.
	'''

	mp = figure(title = "Chicago" + stat + "Crime")

	data_set = pd.read_csv('chicago_crime_2018.csv', index = "ID")

	x_coords = data_set.as_matrix(columns = data_set.columns('Longitude'))

	y_coords = data_set.as_matrix(columns = data_set.columns('Latitude'))

	mp.circle(x = x_coords, y = y_coords, size = 1, color = "red")






