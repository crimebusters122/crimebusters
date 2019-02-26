### Getting data from BJS for crimebusters ###
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

def get_national_data(csv_filename):
    '''
    '''
    head = ['Year', 'City', 'Department', 'Violent Crime'+\
            ' Total', 'Murder and Nonnegligent Manslaughter', 'Rape', \
            'Robbery', 'Aggravated Assault', 'Property Crime Total', \
            'Burglary', 'Larceny-Theft', 'Motor Vehicle Theft']

    with open(csv_filename, mode='a') as national_data:
        national_writer = csv.writer(national_data, delimiter=',', quoting=csv.QUOTE_ALL)
        #national_writer.writerow(head)

    driver = webdriver.Firefox()
    driver.get('https://www.bjs.gov/index.cfm?ty=datool&surl=/arrests/index.cfm#')
    driver.find_elements_by_xpath("//div[@title='Agency-Level Counts']")[0].click()
    driver.find_elements_by_xpath("//a[@id='atab1']")[0].click()
    time.sleep(3)

    department_code_dict = {"Alabama": ['"AL00201"'], "Alaska": ['"AK00101"'], 
                            "Arizona": ['"AZ00705"', '"AZ00717"', '"AZ01003"', 
                            '"AZ00723"'], 
                            "California": ['"CA03001"', '"CA01502"', '"CA03702"', 
                            '"CA01941"', '"CA00109"', '"CA03313"', '"CA03404"', 
                            '"CA03019"', '"CA03905"', '"CA01005"', '"CA03800"', 
                            '"CA01942"', '"CA03711"', '"CA04313"'], 
                            "Colorado": ['"CO00101"', '"CODPD00"',
                            '"CO02101"'], "Florida": ['"FL01306"', '"FL04804"',
                            '"FL02902"', '"FL01602"'], "Georgia": ['"GAAPD00"'], 
                            "Indiana": ['"IN00201"', '"INIPD00"'], 
                            "Kansas": ['"KS08703"'], "Kentucky": ['"KY05602"'], 
                            "Louisiana": ['"LANPD00"'], "Minnesota": 
                            ['"MN02711"', '"MN06209"'], "Missouri": ['"MOSPD00"'],
                            "North Carolina": ['"NC04102"', '"NC09201"', '"NC06001"'], 
                            "Nebraska": ['"NB05501"', '"NB02802"'], "New Jersey": 
                            ['"NJ00906"', '"NJNPD00"'], "Nevada": ['"NV00203"', 
                            '"NV00201"'],
                            "New York": ['"NY01401"', '"NY03030"'], 
                            "Ohio": ['"OHCIP00"', 
                            '"OHCLP00"', '"OH04807"', '"OHCOP00"'], 
                            "Oklahoma": ['"OK07205"', '"OK05506"'],
                            "Pennsylvania": ['"PAPPD00"', '"PAPEP00"'], 
                            "Texas": ['"TX22001"', '"TXDPD00"', '"TXHPD00"',
                            '"TX17802"', '"TX24001"', '"TX04306"', '"TXSPD00"',
                            '"TX22701"', '"TX22012"', '"TX07102"'], "Virginia": 
                            ['"VA12800"'], "District of Columbia": ['"DCMPD00"'],
                            "Hawaii": ['"HI00200"'], "Massachusetts": ['"MA01301"'],
                            "Maryland": ['"MDBPD00"'], "Michigan": ['"MI82349"'],
                            "New Mexico": ['"NM00101"'], "Oregon": ['"OR02602"'],
                            "Tennessee": ['"TNMPD00"', '"TN01901"'], 
                            "Washington": ['"WASPD00"'], "Wisconsin": ['"WIMPD00"'],
                            "Illinois": ['"ILCPD00"'],}

    grab_from_site = ['Violent Crime Index', 'Murder and Non-Negligent' +\
    ' Manslaughter', 'Forcible Rape', 'Robbery', 'Aggravated Assault', 'Property' +\
    ' Crime Index', 'Larceny-Theft', 'Motor Vehicle Theft']

    for option in range (0, 50):
        driver.find_elements_by_xpath("//option[@value="+str(option)+"]")[0].click()
        state = driver.find_elements_by_xpath(
            "//option[@value="+str(option)+"]")[0].text 
        if state in department_code_dict:
            print(state)
            time.sleep(5)
            for department_code in department_code_dict[state]:
                print(department_code)
                button = driver.find_elements_by_xpath(
                    "//option[@value="+department_code+"]")[0]
                button.click()
                department = button.text
                print(department)
    '''
    for year in range(1980, 2015):
        data_list = [str(year), 'United States-Total', 'N/A']
        driver.find_elements_by_xpath("//option[@value="+str(year)+"]")[0].click()
        driver.find_elements_by_xpath("//a[@title='Generate Results']")[0].click()
        time.sleep(18)
        for thing in grab_from_site:
            alpha = driver.find_elements_by_xpath("//td[@title='" +\
        	    thing + " -- Total all ages']")[0].text
            data_list.append(alpha)
        with open(csv_filename, mode='a') as data:
            data_writer = csv.writer(data, delimiter=',', quoting = csv.QUOTE_ALL)
            data_writer.writerow(data_list)

    '''
get_national_data('bjs_city.csv')
