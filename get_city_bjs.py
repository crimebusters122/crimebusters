### Getting data from BJS for crimebusters ###
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

def get_city_data(csv_filename):
    '''
    '''
    head = ['Year', 'City', 'Violent Crime'+\
            ' Total', 'Murder and Nonnegligent Manslaughter', 'Rape', \
            'Robbery', 'Aggravated Assault', 'Property Crime Total', \
            'Burglary', 'Larceny-Theft', 'Motor Vehicle Theft']

    with open(csv_filename, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(head)

    driver = webdriver.Firefox()
    driver.get('https://www.bjs.gov/index.cfm?ty=datool&surl=/arrests/index.cfm#')
    driver.find_elements_by_xpath("//div[@title='Agency-Level Counts']")[0].click()
    time.sleep(2)
    driver.find_elements_by_xpath("//a[@id='atab1']")[0].click()
    time.sleep(3)
    asdf = driver.find_elements_by_xpath("//option[@value=1]")
    for a in asdf:
        if a.text == "Offense By Age":
            a.click()
            break

    department_code_dict = {"Alabama": ['"AL00201"'], "Alaska": ['"AK00101"'], 
                            "Arizona": ['"AZ00705"', '"AZ00717"', '"AZ01003"', 
                            '"AZ00723"'], 
                            "California": ['"CA03001"', '"CA01502"', '"CA03702"', 
                            '"CA01941"', '"CA00109"', '"CA03313"', '"CA03404"', 
                            '"CA03019"', '"CA03905"', '"CA01005"', '"CA03801"', 
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
    state_keys = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', \
                 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', \
                 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', \
                 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': \
                 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', \
                 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', \
                 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', \
                 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', \
                 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', \
                 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': \
                 'NM', 'New York': 'NY', 'North Carolina': 'NC', \
                 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', \
                 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina':\
                  'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': \
                 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', \
                 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI',\
                  'Wyoming': 'WY', 'District of Columbia': 'DC'}
    weird_names = {'TX22012': 'Fort Worth, TX', 'CA03702': \
                    'Chula Vista, CA', 'CA01941': 'Long Beach, CA', \
                    'CA03019': 'Santa Ana, CA', 'CO02101': \
                    'Colorado Springs, CO', 'IN00201': 'Fort Wayne, IN', \
                    'LANPD00': 'New Orleans, LA', 'MN06209': 'St. Paul, MN', \
                    'MOSPD00': 'St. Louis, MO', 'NJ00906': 'Jersey City, NJ', \
                    'TX17802': 'Corpus Christi, TX', 'VA12800': \
                    'Virginia Beach, VA', 'CA03801': 'San Francisco, CA', \
                    'OK05506': 'Oklahoma City, OK', 'TX07102': 'El Paso, TX', \
                    'CA01942': 'Los Angeles, CA', 'CA03711': 'San Diego, CA', \
                    'CA04313': 'San Jose, CA', 'NV00201': 'Las Vegas, NV', \
                    'NY03030': 'New York City, NY', 'TXSPD00': \
                    'San Antonio, TX'}

    grab_from_site = ['Violent Crime Index', 'Murder and Non-Negligent' +\
    ' Manslaughter', 'Forcible Rape', 'Robbery', 'Aggravated Assault', 'Property' +\
    ' Crime Index', 'Burglary', 'Larceny-Theft', 'Motor Vehicle Theft']

    for option in range (0, 50):
        driver.find_elements_by_xpath("//option[@value="+str(option)+"]")[0].click()
        state = driver.find_elements_by_xpath(
            "//option[@value="+str(option)+"]")[0].text 
        if state in department_code_dict:
            time.sleep(5)
            for department_code in department_code_dict[state]:
                button = driver.find_elements_by_xpath(
                    "//option[@value="+department_code+"]")
                if len(button) != 0:
                    button[0].click()
                if department_code not in weird_names:
                    city = button[0].text.split()[0] + ', ' + state_keys[state]
                else:
                    city = weird_names[department_code]
                department = button[0].text
                for year in range(2001, 2015):
                    data_list = [str(year), city]
                    driver.find_elements_by_xpath(
                        "//option[@value="+str(year)+"]")[0].click()    
                    driver.find_elements_by_xpath(
                        "//a[@title='Generate Results']")[0].click()
                    time.sleep(18)
                    for thing in grab_from_site:
                        alpha = driver.find_elements_by_xpath("//td[@title='" +\
        	                thing + " -- Total all ages']")
                        if len(alpha) != 0:
                            data_list.append(alpha[0].text)
                    with open(csv_filename, mode='a') as data:
                        data_writer = csv.writer(data, 
                            delimiter=',', quoting = csv.QUOTE_ALL)
                        data_writer.writerow(data_list)
    driver.close()
