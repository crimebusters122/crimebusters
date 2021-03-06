### Gets data from OJJDP for crimebusters ###
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

def get_raw_national_data(starting_years, target_dir):
    '''
    Gets national crime data from OJJDP

    Inputs:
        starting_years: (iterable) Either the list [1994,2001,2008] or
                        a sublist. Years should be given in ascending order
                        Note: including 2008 would get 2008-2014
        target_dir: (string) Path to the directory for storing raw csv files
    '''
    #credit for custom profile: https://selenium-python.readthedocs.io/faq.html
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList",2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", target_dir)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('https://www.ojjdp.gov/ojstatbb/ezaucr/asp/ucr_display.asp')
    for start in starting_years:
        state_object = driver.find_element_by_xpath("//option [@value=0]")
        state_object.click()
        year_object = driver.find_element_by_xpath("//input [@name='rdoYear'] \
            [@VALUE="+str(start)+"]")
        year_object.click()
        age_object = driver.find_element_by_xpath("//input [\
            @name='rdoData'] [@VALUE='1c']")
        age_object.click()
        update_object = driver.find_element_by_xpath("//button \
            [@name='submit'] [@value='Update Table']")
        update_object.click()
        data_object = \
            driver.find_element_by_xpath("//a [@title='Download CSV file']")
        data_object.click()
    driver.close()
    return

def clean_csv(starting_years, target_dir, new_csv):
    '''
    Combine csv outputs from above code, turn them so each row is a year

    Inputs:
        starting_years: (iterable) As above
        target_dir: (string) As above
        new_csv: (string) Path to new csv to be written to
    '''
    NUM_ROWS_TO_USE = 34 #number of rows in csv containing data
    df_list = []
    for i in range(len(starting_years)):
        if i == 0:
            csv_name = target_dir + '/ucr_export.csv'
        else:
            csv_name = target_dir + '/ucr_export(' + str(i) + ').csv'
        df = pd.read_csv(csv_name,header=1,index_col=0,nrows=NUM_ROWS_TO_USE)
        df.drop('Unnamed: 8', axis=1, inplace=True)
        df = df.transpose()
        df_list.append(df)
        big_df = pd.concat(df_list)
        big_df.rename({'Prostitution/<br>commercialized vice':\
            'Prostitution/commercialized vice'},axis=1,inplace=True)
        big_df.to_csv(new_csv, index_label=False, \
            header=['Year']+list(big_df.columns)[1:])
    return

def get_clean_csv(starting_years, target_dir, new_csv):
    '''
    Get a cleaned csv of national data

    Inputs:
        starting_years: (iterable) Either the list [1994,2001,2008] or
                        a sublist. Years should be given in ascending order
                        Note: including 2008 would get 2008-2014
        target_dir: (string) Path to the directory for storing raw csv files
        new_csv: (string) Path to file where cleaned csv should be written
    '''
    get_raw_national_data(starting_years, target_dir)
    clean_csv(starting_years, target_dir, new_csv)
    return