### Create statistic vs. statistic plots for website ###
import sqlite3 as sql
import matplotlib.pyplot as plt


def make_graph(type1, loc_type1, stat1, loc1, type2, loc_type2, stat2, loc2):
    '''
    Create the graph comparing the two statistics

    Inputs:
        type1: (string) The type of statistic, (ie: 'crime', 'arrest')
        stat1: (string) The actually statistic (ie: 'Robbery')
        type2: (string) The same as type1, but for the second statistic
        stat2: (string) The same as stat1, but for the second statistic
    '''
    DATABASE = './db/crimebusters_data.db'
    ARREST = {'city' : 'bjs_city',
              'national' : 'national_arrests'}
    CRIME = {'city' : 'cities_data',
             'state' : 'states_data',
             'national' : 'states_data'}
    tables = {'arrest' : ARREST,
              'crime' : CRIME}

    db = sql.connect(DATABASE)
    c = db.cursor()

    stat1 = stat1.replace(' ','_')
    stat2 = stat2.replace(' ','_')
    params = []

    if type2 != 'time':
        query, params = make_query(type1, loc_type1, stat1, loc1, type2, \
            loc_type2, stat2, loc2)
        data = c.execute(query,params)
        data1 = []
        data2 = []
        for elem in data:
            if (elem[0] != 'nan') and (elem[1] != 'nan'):
                data1.append(int(elem[0].replace(',','')))
                data2.append(int(elem[1].replace(',','')))
        plt.plot(data1,data2)
        plt.show()
    else:
        table2 = None
        query = 'SELECT Year,'+stat1+' FROM '+table1
        if table1 != 'national_arrests':
            query = query + ' WHERE '+loc_type1+' = ?;'
            params = [loc1]
            data = c.execute(query, params)
        else:
            query = query + ';'
            data = c.execute(query, params)
        plt.plot(data)
        plt.show()

    db.close()
    return


def make_query(type1, loc_type1, stat1, loc1, type2, loc_type2, stat2, loc2):
    ARREST = {'city' : 'bjs_city',
              'national' : 'national_arrests'}
    CRIME = {'city' : 'cities_data',
             'state' : 'states_data',
             'national' : 'states_data'}
    tables = {'arrest' : ARREST,
              'crime' : CRIME}

    table1 = tables[type1][loc_type1]
    table2 = tables[type2][loc_type2]
    params = []
    query = 'SELECT '+table1+'.'+stat1+', '+table2+'.'+stat2+' FROM '
    if table1 == table2:
        query = query + table1
    else:
        query = query+table1+' JOIN '+table2+' ON '+table1\
        +'.Year = '+table2+'.Year'
    if table1 == 'states_data':
        query = query + ' WHERE states_data.State = ?'
        params.append(loc1)
    elif table1 != 'national_arrests':
        query = query + ' WHERE '+table1+'.City = ?'
        params.append(loc1)
    elif table2 != 'national_arrests':
        query = query + ' WHERE '
    if table2 == 'states_data':
        if query[-1] == '?':
            query = query + ' AND '
        query = query + 'states_data.State = ?;'
        params.append(loc2)
    elif table2 != 'national_arrests':
        if query[-1] == '?':
            query = query + ' AND '
        query = query+table2+'.City = ?;'
        params.append(loc2)
    else:
        query = query + ';'

    return query, params


def clean_data(l):
    '''
    Fills in missing data for years 2001-2014 with linear
    approximation to make plot look nice for stat vs. time graphs

    NOTICE: If missing years are on the end, they are excluded

    Inputs:
        l: (list) the list of elements (year,stat) to be cleaned, years in
                  ascending order

    Returns:
        rtn: (list) the cleaned list
    '''
    first_year = int(l[0][0])
    return_length = int(l[-1][0]) - first_year + 1 #number of years in plot

    rtn = [None]*return_length
    d = dict(l)
    for year,stat in d.items():
        rtn[int(year)-first_year] = int(stat.replace(',',''))
    for i in range(len(rtn)):
        if rtn[i] == None: #specify None in case value is 0
            last,nxt = last_next_value(rtn, i)
            time = nxt - last
            last_year = str(last + first_year)
            next_year = str(nxt + first_year)
            last_stat = int(d[last_year].replace(',',''))
            next_stat = int(d[next_year].replace(',',''))
            difference = next_stat - last_stat
            slope = round(difference/time)
            print(slope)
            for j in range(time-1):
                ind = i+j
                rtn[ind] = slope*(ind-last) + rtn[last]

    return rtn

def last_next_value(l, ind):
    '''
    Finds the index of the last element before the given index 
    in the list that was not None. As this is used above, last should
    always be ind-1, but this is to be safe/generalizable.

    Inputs:
        l: (list) the list to examine
        ind: (int) the index around which we are looking

    Outputs:
        rtn: (tuple) the last and next non-None index before the given spot,
                     in the order (last, next)
    '''

    for i in range(1,len(l)):
        if l[ind-i] != None: #specify None-type in case value is 0,
            last = ind-i     #since that would also be False
            break
    for i in range(1,len(l)):
        if l[ind+i] != None:
            nxt = ind+i
            break

    if last == ind-1:
        print('last is ind-1')
    else:
        print('last is NOT ind-1')

    return (last,nxt)