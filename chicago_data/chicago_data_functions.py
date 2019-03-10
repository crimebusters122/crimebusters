import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import geopandas as gpd
from bokeh.plotting import figure, save
from bokeh.models import ColumnDataSource, HoverTool
import folium



def linear_regression(x,y):
    '''
    Makes a linear regression table
    '''

    model = sm.OLS(y, x).fit()

    return model.summary()



def map_of_chicago_crime(c_type = 'every', year_min = 2001, year_max = 2018,\
    arrest = 'irrelelevant'):
    '''
    Makes a map of the density of a crime in Chicago.  Clicking on a dot/
        neighborhood will give you more indepth information.
    '''

    mp = gdp.read_file('Neighborhoods_2012b.shp')

    data_set = pd.read_csv('chicago_crime_2018.csv', index = "ID")

    x_coords = data_set.as_matrix(columns = data_set.columns('Longitude'))

    y_coords = data_set.as_matrix(columns = data_set.columns('Latitude'))

    mp.circle(x = x_coords, y = y_coords, size = 1, color = "red")


    return save(obj = mp, filename = 'crime_map')


def chicago_map():
    '''
    '''

    file_path = "Neighborhoods_2012b.shp"
    geo_data = gpd.read_file(file_path)

    geo_data['x'] = geo_data.apply(get_poly_coords, coord = 'x', axis = 1)
    geo_data['y'] = geo_data.apply(get_poly_coords, coord = 'y', axis = 1)

    return(geo_data)

    #cols_to_drop = ['PRI_NEIGH', 'SEC_NEIGH', 'geometry']
    #usable_geo_data = pd.DataFrame(geo_data.drop(cols_to_drop, axis = 1))
    #mpsource = ColumnDataSource(usable_geo_data)
    #mp = figure(title = 'Chicago')
    #mp.multiline('x', 'y', source = mpsource, color = 'red', line_width = 1)

    #return save(obj = mp, filename = 'crime_map')


def get_poly_coords(row, coord, geometry = 'geometry'):
    '''
    Returns the x or y coordinates of the edges of a polygon
    '''

    boundary = row[geometry].boundary

    if coord == "x":
        return list(boundary.coords.xy[0])
    if coord == "y":
        return list(boundary.coord.xy[1])



def folium_map_chicago():
	'''
	'''

	chicago_coordinates = (41.881832, -87.623177)
	data_set = pd.read_csv('chicago_crime_2018.csv')

	max_records = 1000

	mp = folium.Map(location = chicago_coordinates, zoom_start = 10)

	for crime in data_set[0:max_records].iterrows():
		folium.Marker(
			location = [crime[1]['Latitude'], crime[1]['Longitude']], 
		).add_to(mp)
	return mp






