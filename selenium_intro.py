# Selenium Tutorial #1
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://sites.google.com/chromium.org/driver/

#########################################################################
#                 FIRST SELENIUM/PYTHON SCRIPT                          #
#     TASK: CRAWL THROUGH MY OWN GITHUB PROFILE AND RETRIEVE DATA       #
#########################################################################

service = Service(executable_path="C:/webdriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.maximize_window()

#go to google.com and search ege bozdemir
driver.get("https://google.com")
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("ege bozdemir" + Keys.ENTER)


#go to github link when search results are displayed
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Ege Bozdemir egebozdemir"))
)
gh_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Ege Bozdemir egebozdemir")
gh_link.click()



#grab user name, contact info
readme_article = driver.find_element(By.XPATH, "//article[@class='markdown-body entry-content container-lg f5']")
rm_article_text = readme_article.text
print(rm_article_text)


#go to repositories
#WebDriverWait(driver, 5).until(
#    EC.presence_of_element_located((By.XPATH, "//ul//li//a[@id='repositories-tab']"))
#)
#driver.find_element(By.XPATH, "//a[@id='repositories-tab']").click()
#repos_tab = driver.find_element(By.XPATH, "//ul//li//a[@id='repositories-tab']")
#repos_tab.click()

time.sleep(10)
driver.quit()

