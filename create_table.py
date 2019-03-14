### Creates a table in the database from a CSV file ###
import csv
import sqlite3
import pandas as pd

def create_table(csv_path, database_path, table_name):
    db = sqlite3.connect(database_path)
    c = db.cursor()
    table = pd.read_csv(csv_path)
    columns = tuple(table.columns)
    c_list = []
    for element in columns:
        c_list.append(element.title().replace(' ','_'))
    columns = tuple(c_list)
    c.execute('DROP TABLE IF EXISTS '+table_name+';')
    table_info = table_name+' '+str(columns)
    query = 'CREATE TABLE '+table_info+';'
    c.execute(query)
    placeholder_l = []
    for j in range(len(columns)):
        placeholder_l.append('?')
    placeholder_l = ','.join(placeholder_l)
    placeholder = '('+ placeholder_l + ')'
    for i in range(table.shape[0]):
        values = tuple([str(v) for v in list(table.iloc[i])])
        c.execute('INSERT INTO '+table_info+' VALUES'+placeholder+';',values)
    db.commit()
    db.close()
    return