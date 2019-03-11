### Create statistic vs. statistic plots for website ###
import sqlite3 as sql
import matplotlib.pyplot as plt


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