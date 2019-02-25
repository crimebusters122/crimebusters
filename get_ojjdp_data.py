### Gets data from OJJDP for crimebusters ###
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_national_data(starting_years, target_dir):
    '''
    Gets national crime data from OJJDP

    Inputs:
        starting_years: (iterable) Either the list [1994,2001,2008] or
                        a sublist. ie: including 2008 would get 2008-2014
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