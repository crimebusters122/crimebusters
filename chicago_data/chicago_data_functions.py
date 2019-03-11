import numpy as np 
import pandas as pd 
import folium
import folium.plugins




def map_chicago_crime(
	quick = False, 
	num = 1000, 
	file = 'chicago_crime_2018.csv',
	prim_type = False,
	):
    '''
    '''

    chicago_coordinates = (41.881832, -87.623177)
    data_set = pd.read_csv(file)

    mp = folium.Map(location = chicago_coordinates, zoom_start = 10)

    if prim_type:
    	data_set = data_set.loc[lambda data_set: \
    	data_set['Primary Type'] == prim_type]

    to_sample = min(num, len(data_set.index))

    geographical_crimes = data_set.dropna().sample(to_sample)

    if quick or num > 5000:
    	locations = []
    	for crime in geographical_crimes.iterrows():
    		locations.append([crime[1]['Latitude'], crime[1]['Longitude']])

    	marker_cluster = folium.plugins.FastMarkerCluster(locations)
    else:
        marker_cluster = folium.plugins.MarkerCluster()

        for crime in geographical_crimes.iterrows():
            primary_type = crime[1]['Primary Type']
            date = crime[1]['Date']
            marker_cluster.add_child(folium.Marker(
                location = [crime[1]['Latitude'], crime[1]['Longitude']], 
                tooltip = '<b>' + "Type of crime: " + primary_type + \
                    "--- Date: " + date
            ))

    mp.add_child(marker_cluster)

    return mp




