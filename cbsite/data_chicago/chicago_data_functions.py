import numpy as np 
import pandas as pd 
import folium
import folium.plugins
from folium.plugins import MarkerCluster, FastMarkerCluster
import sqlite3


def map_chicago_crime_db(
    quick = False, 
    num = 1000, 
    year = None,
    prim_type = False,
    ):
    '''
    Makes an interactive Folium map of Chicago.

    Inputs:
        quick (bool): whether to include a tooltip over the points on the map
        num (int): The number of points you want to see
        year (int or bool): The year you want to look at
        prim_type (str of bool): The type of crime you want to look at

    Output:
        A Folium map object
    '''

    data_base_path = '/home/student/crimebusters/chicago_db/chicago_crime.db'
    chicago_coordinates = (41.881832, -87.623177)

    db_connection = sqlite3.connect(data_base_path)
    db_cursor = db_connection.cursor()

    mp = folium.Map(location = chicago_coordinates, zoom_start = 10)

    query = construct_query('crime', quick, year, prim_type)

    print(query)

    r = db_cursor.execute(query, [num])
    print(r)

    data = r.fetchall()
    if len(data) == 0:
        return "No such crimes exist for these parameters!"

    if quick:
        usable_data = []
        for loc in data:
            usable_data.append([float(loc[0]), float(loc[1])])
        print(usable_data[0][0:5], usable_data[1][0:5])
        marker_cluster = folium.plugins.FastMarkerCluster(usable_data)

    else:
        marker_cluster = folium.plugins.MarkerCluster()

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


def construct_query(table, quick, year, prim_type):
    '''
    Constructs a query to get the information we want out of the database/
    '''

    query = "SELECT Latitude, Longitude"

    if not quick:
        query += ", \"Primary.Type\", Date"

    query += " FROM " + table + " WHERE"

    query += " rowid IN (SELECT rowid FROM " + table

    if year:
        query += " WHERE Year = \'" + str(year) +"\'"
    if prim_type and not year:
        query += " WHERE \"Primary.Type\" = \'" + prim_type + "\'"
    if prim_type and year:
        query += " AND \"Primary.Type\" = \'" + prim_type + "\'"

    query += " ORDER BY RANDOM()" + " LIMIT ?);"

    return query


