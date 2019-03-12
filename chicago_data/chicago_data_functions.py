import numpy as np 
import pandas as pd 
import folium
import folium.plugins
import sqlite3




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




def map_chicago_crime_db(
    quick = False, 
    num = 1000, 
    year = None,
    prim_type = False,
    ):
    '''
    '''

    data_base_path = 'chicago_crime.db'
    chicago_coordinates = (41.881832, -87.623177)

    db_connection = sqlite3.connect(data_base_path)
    db_cursor = db_connection.cursor()


    mp = folium.Map(location = chicago_coordinates, zoom_start = 10)

    query = construct_query('crime', quick, num, year, prim_type)

    print(query)

    r = db_cursor.execute(query)

    if quick:
        marker_cluster = folium.plugins.FastMarkerCluster(r.fetchall())
    else:
        marker_cluster = folium.plugins.MarkerCluster()

        data = r.fetchall()
        print(data[0])

        for crime in range(len(data)):

            primary_type = data[crime][2]
            date = data[crime][3]
            marker_cluster.add_child(folium.Marker(
                location = [float(data[crime][0]), float(data[crime][1])], 
                tooltip = '<b>' + "Type of crime: " + primary_type + \
                    "--- Date: " + date 
            ))

    mp.add_child(marker_cluster)

    db_connection.close()

    return mp


def construct_query(table, quick, num, year, prim_type):
    '''
    Constructs a query to get the information we want out of the database/
    '''

    query = "SELECT Latitude, Longitude"

    if not quick:
        query += ", [Primary.Type], Date"

    query += " FROM " + table + " WHERE Latitude != \"NA\" AND " 
    query += "rowid IN (SELECT rowid FROM " + table + " ORDER BY RANDOM()" 
    query += " LIMIT " + str(num) + ")"

    if year:
        query += " AND Year >= " + str(year[0]) +" AND Year <= " + str(year[1])
    if prim_type:
        query += " AND [Primary.] = " + prim_type +";"

    return query


