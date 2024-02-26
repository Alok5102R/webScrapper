from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from openpyxl import Workbook


# Set up the Chrome driver (Make sure you have Chrome WebDriver installed)
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# URL of the website containing job listings
url = 'https://www.naukri.com/it-jobs'

driver.get(url)

time.sleep(2)

# div_elements = driver.find_element(By.CLASS_NAME, "title") # It'll fetch single Element
div_elements = driver.find_elements(By.CLASS_NAME, "title") # It'll fetch multiple Elements and put them in list
div1_elements = driver.find_elements(By.CLASS_NAME, "job-desc") 


# Create a new workbook
wb = Workbook()

# Select the active worksheet
ws = wb.active
i=1
for div in div_elements:
    ws.append([i,div.text])
    i+=1
i=1
for div in div1_elements:
    ws.cell(row=i, column=3, value=div.text)
    i+=1

# Save the workbook
wb.save('example.xlsx')

# # Quit the browser
driver.quit()