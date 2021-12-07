import pandas as pd
import re

from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from IPython.core.display import clear_output
from random import randint
from requests import get
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import time
start_time = time()


for m in range(33,41):
    print(m)
    print('=====')
    stt = 25*m
    url = 'https://www.linkedin.com/jobs/search/?geoId=101318387&keywords=computer%20science&location=Florida%2C%20United%20States&start=' + str(stt)

    no_of_jobs = 25

    # this will open up new window with the url provided above
    driver = webdriver.Chrome(executable_path=r"E:\Python\chromedriver.exe")
    driver.get(url)
    sleep(3)
    action = ActionChains(driver)

  
    i = 2
    while i <= (no_of_jobs / 25):
        driver.find_element_by_xpath('/html/body/main/div/section/button').click()
        i = i + 1
        sleep(5)


    pageSource = driver.page_source
    lxml_soup = BeautifulSoup(pageSource, 'lxml')


    job_container = lxml_soup.find('ul', class_='jobs-search__results-list')

    print('You are scraping information about {} jobs.'.format(len(job_container)))


    post_title = []
    job_id = []
    job_location = []
    job_desc = []
    functions = []

   
    for job in job_container:

        job_ids = job.find('a', href=True)['href']
        job_ids = re.findall(r'(?!-)([0-9]*)(?=\?)', job_ids)[0]
        job_id.append(job_ids)


        job_titles = job.find("span", class_="screen-reader-text").text
        post_title.append(job_titles)

        job_locations = job.find("span", class_="job-result-card__location").text
        job_location.append(job_locations)


    for x in range(1, len(job_id) + 1):
        # click on different job containers to view information about the job
        job_xpath = '/html/body/main/div/section/ul/li[{}]/img'.format(x)
        driver.find_element_by_xpath(job_xpath).click()
        sleep(3)

        jobdesc_xpath = '/html/body/main/section/div[2]/section[2]/div'
        job_descs = driver.find_element_by_xpath(jobdesc_xpath).text
        job_desc.append(job_descs)

     
        job_criteria_container = lxml_soup.find('ul', class_='job-criteria__list')
        all_job_criterias = job_criteria_container.find_all("span",
                                                            class_='job-criteria__text job-criteria__text--criteria')


        function_xpath = '/html/body/main/section/div[2]/section[2]/ul/li[3]'
        job_function = driver.find_element_by_xpath(function_xpath).text.splitlines(0)[1]
        functions.append(job_function)
        sleep(3)

        x = x + 1


    if True:
        job_data = pd.DataFrame({'Job ID': job_id,
                                 'Post': post_title,
                                 'Location': job_location,
                                 'Description': job_desc,
                                 'Function': functions
                                 })


    job_data['Description'] = job_data['Description'].str.replace('\n', ' ')

    print(job_data.info())
    job_data.head()

    out_name = 'LinkedIn Job Data' + str(m) + '.csv'

    job_data.to_csv(out_name, index=0)




