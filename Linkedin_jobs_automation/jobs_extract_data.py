from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd


web = 'https://in.linkedin.com/jobs/software-engineer-jobs-greater-chennai-area?position=1&pageNum=0'
path = "E:\selenium\chromedriver.exe"  # introduce chromedriver path here

# Creating the driver

driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)

#fitering entry level jobs
driver.find_element(by='xpath', value='//ul[@class="filters__list"]/li[6]/div/div/button').click()
driver.find_element(by='xpath', value='//ul[@class="filters__list"]/li[6]/div/div/div/div/div/div[2]/label').click()#entry level
driver.find_element(by='xpath', value='//*[@id="jserp-filters"]/ul/li[6]/div/div/div/button').click()

# Finding elements
containers=driver.find_elements(by="xpath",value='//ul[@class="jobs-search__results-list"]/li/div/div[2]')

#Lists store the values
job_titles = []
company_names = []
links =[]

for container in containers:
    job_title=container.find_element(by="xpath",value='./h3').text #job title
    company_name=container.find_element(by="xpath",value='./h4').text  #company name
    link=container.find_element(by="xpath",value='./h4/a').get_attribute("href") #link
    #appending the values into the list
    job_titles.append(job_title)
    company_names.append(company_name)
    links.append(link)
    
# Exporting data to a CSV file
my_dict = {'Job Title': job_titles, 'Company Name': company_names, 'Links': links }
df_joblist = pd.DataFrame(my_dict)
df_joblist.to_csv('Linkedin_jobs.csv')

driver.quit()
