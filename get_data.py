### Getting data from UCR for crimebusters ###
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

def get_state_data(state, csv_filename):
    driver = webdriver.Firefox()
    driver.get('https://www.ucrdatatool.gov/Search/Crime/State/StatebyState.cfm')
    if state != 'United States-Total':
        c = "[contains(text(), '" + state + "')]"
        state_object = driver.find_elements_by_xpath("//select"+\
                       "[@name='StateId']/*"+c)[0]
    else:
        state_object = driver.find_elements_by_xpath("//select"+\
                       "[@name='StateId']/option[@value='52']")[0]
    state_object.click()
    for choice in range(1, 5):
        string = str(choice)
        data_object = driver.find_elements_by_xpath("//select[@name="+\
                      "'DataType']/option[@value= "+string+"]")[0]
        data_object.click()
    year_start = driver.find_elements_by_xpath("//select[@name='YearStart']"+\
                "/option[@value='2001']")[0]
    year_start.click()
    year_end = driver.find_elements_by_xpath("//select[@name='YearEnd']"+\
                "/option[@value='2014']")[0]
    year_end.click()
    next_page = driver.find_elements_by_xpath("//input[@name='NextPage' and "+\
                "@type='submit']")[0]
    next_page.click()
    yrs = driver.find_elements_by_xpath("//td[@headers='year']")
    pops = driver.find_elements_by_xpath("//td[@headers='population']")
    v_nums = driver.find_elements_by_xpath("//td[@headers="+\
                  "'num vcrime1 vctot']")
    murd_nums = driver.find_elements_by_xpath("//td[@headers="+\
                 "'num vcrime1 murd']")
    rape_nums = driver.find_elements_by_xpath("//td[@headers="+\
                      "'num vcrime1 rape']")
    rob_nums = driver.find_elements_by_xpath("//td[@headers="+\
                   "'num vcrime1 rob']")
    aslt_nums = driver.find_elements_by_xpath("//td[@headers="+\
                        "'num vcrime1 aggr']")
    p_nums = driver.find_elements_by_xpath("//td[@headers="+\
                          "'num pcrime1 pctot']")
    burg_nums = driver.find_elements_by_xpath("//td[@headers="+\
                    "'num pcrime1 burg']")
    larc_nums = driver.find_elements_by_xpath("//td[@headers="+\
                   "'num pcrime1 larc']")
    mv_nums = driver.find_elements_by_xpath("//td[@headers="+\
                    "'num pcrime1 mvtheft']")
    v_rts = driver.find_elements_by_xpath("//td[@headers="+\
                   "'rate vcrime2 vctot2']")
    murd_rts = driver.find_elements_by_xpath("//td[@headers="+\
                  "'rate vcrime2 murd2']")
    rape_rts = driver.find_elements_by_xpath("//td[@headers="+\
                       "'rate vcrime2 rape2']")
    rob_rts = driver.find_elements_by_xpath("//td[@headers="+\
                    "'rate vcrime2 rob2']")
    aslt_rts = driver.find_elements_by_xpath("//td[@headers="+\
                         "'rate vcrime2 aggr2']")
    p_rts = driver.find_elements_by_xpath("//td[@headers="+\
                    "'rate pcrime2 pctot2']")
    burg_rts = driver.find_elements_by_xpath("//td[@headers="+\
                     "'rate pcrime2 burg2']")
    larc_rts = driver.find_elements_by_xpath("//td[@headers="+\
                    "'rate pcrime2 larc2']")
    mv_rts = driver.find_elements_by_xpath("//td[@headers="+\
                     "'rate pcrime2 mvtheft2']")
    list_of_data = []
    for n in range(0, 14):
        list_of_data.append([yrs[n].text] + [state] + [pops[n].text] + [v_nums[n].text] + \
            [murd_nums[n].text] + [rape_nums[n].text] + [rob_nums[n].text] + \
            [aslt_nums[n].text] + [p_nums[n].text] + [burg_nums[n].text] + \
            [larc_nums[n].text] + [mv_nums[n].text] + [v_rts[n].text] + \
            [murd_rts[n].text] + [rape_rts[n].text] + [rob_rts[n].text] + \
            [aslt_rts[n].text] + [p_rts[n].text] + [burg_rts[n].text] + \
            [larc_rts[n].text] + [mv_rts[n].text])
    with open(csv_filename, mode='a') as states_data:
        states_writer = csv.writer(states_data, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in range(0, 14):
            states_writer.writerow(list_of_data[i])
    driver.close()

def get_all_states(csv_filename):
    states = ['United States-Total', 'Alabama', 'Alaska', 'Arizona', \
             'Arkansas', 'California', 'Colorado', 'Connecticut', \
             'Delaware', 'District of Columbia', 'Florida', 'Georgia', \
             'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', \
             'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', \
             'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', \
             'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', \
             'New Mexico', 'New York', 'North Carolina', 'North Dakota', \
             'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', \
             'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', \
             'Vermont', 'Virginia', 'Washington', 'West Virginia', \
             'Wisconsin', 'Wyoming']
    head = ['Year', 'Population', 'Violent Crime Total', 'Murder and ' + \
            'Nonnegligent Manslaughter', 'Rape', 'Robbery', 'Aggravated ' +\
             'Assault', 'Property Crime Total', 'Burglary', 'Larceny-Theft', \
             'Motor Vehicle Theft', 'Violent Crime Rate', 'Murder and ' +\
             'Nonnegligent Manslaughter Rate', 'Rape Rate', 'Robbery Rate', \
             'Aggravated Assault Rate', 'Property Crime Rate', 'Burglary '+\
             'Rate', 'Larceny-Theft Rate', 'Motor Vechicle Theft Rate']
    with open(csv_filename, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(head)
    for state in states:
        get_state_data(state, csv_filename)
