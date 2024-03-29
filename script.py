import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import pandas as pd

PATH = 'chromedriver.exe path'
browser = webdriver.Chrome(PATH)
browser.get('https://www.linkedin.com/')
browser.maximize_window()
time.sleep(5)

username = browser.find_element('id', 'session_key')
username.send_keys('email')
password = browser.find_element('id', 'session_password')
password.send_keys('password')
browser.find_element(By.CLASS_NAME,'sign-in-form__submit-button').click()
time.sleep(7)

browser.get('https://www.linkedin.com/jobs/search/')
time.sleep(7)

job_search = browser.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
job_search.send_keys('data analyst')
job_loc_search = browser.find_element(By.XPATH, '//input[@aria-label="City, state, or zip code"]')
job_loc_search.clear()
job_loc_search.send_keys('Hanoi')
browser.find_element(By.CLASS_NAME, "jobs-search-box__submit-button").click()
time.sleep(7)

job_lists = []

for page in range(2,4): # range(2, can be change depending on mood) :)
    job_cards = browser.find_elements(By.XPATH, '//ul[@class="scaffold-layout__list-container"]/li') #Class got changed??
    card_ids = [result.get_attribute('id') for result in job_cards] #Get all job ids to let selenium click each job individually
    #print(card_ids)
    for id in card_ids:
        time.sleep(1)
        try:
            job = browser.find_element(By.ID, id)
            job_id = job.get_attribute('data-occludable-job-id')
            browser.find_element(By.XPATH, f'//div[@data-job-id={job_id}]').click() #Click on each job for the html to show the card
        except:
            continue

        try:
            job_title = browser.find_element(By.XPATH, "//h2[@class='t-24 t-bold jobs-unified-top-card__job-title']").text
        except:
            job_title = ''
            #time.sleep(5)
        #print(job_title)

        try:
            sub_card_1 = browser.find_element(By.XPATH, "//span[@class='jobs-unified-top-card__subtitle-primary-grouping mr2 t-black']").find_elements(By.TAG_NAME, 'span')
            job_company = sub_card_1[0].text
            job_location = sub_card_1[1].text
            if (len(sub_card_1) > 2):
                job_worktype = sub_card_1[2].text
            else:
                job_worktype = ''
        except:
            job_company = ''
            job_location = ''
            job_worktype = ''
            #time.sleep(5)
            #print(job_company + " " + job_location + " " + job_worktype)

        try:
            sub_card_2 = browser.find_element(By.XPATH, "//span[@class='jobs-unified-top-card__subtitle-secondary-grouping t-black--light']").find_elements(By.TAG_NAME, 'span')
            job_post_date_from_sd = sub_card_2[0].text
            job_no_of_apps = sub_card_2[1].text
        except:
            job_post_date_from_sd = ''
            job_no_of_apps = ''
            #time.sleep(5)
            #print(job_post_date_from_sd + " " + job_no_of_apps)

        try:
            sub_card_3 = browser.find_elements(By.XPATH, '//div[@class="mt5 mb2"]/ul//li')
            if sub_card_3[0].text != '':
                job_info = sub_card_3[0].text.split(" · ")
                if (len(job_info) == 1):
                    job_salary = ''
                    job_work_dur = job_info[0]
                    job_pos_title = ''
                elif (len(job_info) == 2):
                    job_salary = ''
                    job_work_dur = job_info[0]
                    job_pos_title = job_info[1]
                else:
                    job_salary = job_info[0]
                    job_work_dur = job_info[1]
                    job_pos_title = job_info[2]
            else:
                job_salary = ''
                job_work_dur = ''
                job_pos_title = ''

            if sub_card_3[1].text != '':
                job_info = sub_card_3[1].text.split(" · ")
                if len(job_info) == 2:
                    company_size = job_info[0]
                    company_sector = job_info[1]
                elif len(job_info) == 1:
                    company_size = job_info[0]
                    company_sector = ''
                else:
                    company_size = ''
                    company_sector = ''
            else:
                company_size = ''
                company_sector = ''
        except:
            job_salary = ''
            job_work_dur = ''
            job_pos_title = ''
            company_size = ''
            company_sector = ''
            time.sleep(5)

        job_detail = browser.find_element(By.XPATH, '//div[@id="job-details"]').text
        job_list = [job_title, job_company, job_location, job_worktype, job_work_dur, job_pos_title, job_salary, company_size, company_sector, job_post_date_from_sd, job_no_of_apps, job_detail]
        job_lists.append(job_list)

    browser.find_element(By.XPATH, f'//button[@aria-label="Page {page}"]').click()
    time.sleep(2)

df = pd.DataFrame(job_lists, columns=['Job title', 'Company', 'Working location', 'Work type', 'Post date', 'Number of applicants'])
#df.head()
df.to_csv('linkedin_job_details.csv')