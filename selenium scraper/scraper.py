from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
import time
import pandas as pd

driver = webdriver.Edge('./msedgedriver.exe')
driver.maximize_window()
driver.get('https://www.tripadvisor.com.sg/Restaurants-g294265-Singapore.html')


def load_page(driver):
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight * 0.3)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight * 0.4)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight * 0.5)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight * 0.6)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight * 0.7)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight * 0.8)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight * 0.9)")
    time.sleep(3)


time.sleep(5)
load_page(driver)
# Ensure the entire page is loaded


# RESTAURANT_NAME = '//*[@id="component_2"]/div/div[43]/div/span/div[1]/div[2]/div[1]/div/span/a'
# COST = '//*[@id="component_2"]/div/div[43]/div/span/div[1]/div[2]/div[2]/div/div[2]/span[2]/span'
# TAGS = '//*[@id="component_2"]/div/div[43]/div/span/div[1]/div[2]/div[2]/div/div[2]/span[1]/span'

restaurant_data = []

for pg in range(20):
    for i in range(1, 44):
        current_dict = {}
        BASE_XPATH = f'//*[@id="component_2"]/div/div[{i}]/'
        RESTAURANT_NAME = BASE_XPATH + 'div/span/div[1]/div[2]/div[1]/div/span/a'
        COST = BASE_XPATH + 'div/span/div[1]/div[2]/div[2]/div/div[2]/span[2]/span'
        TAGS = BASE_XPATH + 'div/span/div[1]/div[2]/div[2]/div/div[2]/span[1]/span'
        SPONSOR_TAG = BASE_XPATH + 'div/span/div/div[1]/div[2]/div[1]/div[1]/div/div'
        try:
            driver.find_element(By.XPATH, SPONSOR_TAG) # If sponsored, ignore
            continue
        except:
            pass
        try:
            name = driver.find_element(By.XPATH, RESTAURANT_NAME).text.split(' ', 1)[1]
            href = driver.find_element(By.XPATH, RESTAURANT_NAME).get_attribute('href')
            print(name)
            print(href)
            current_dict['name'] = name
            current_dict['href'] = href
        except:
            continue
        try:
            cost = driver.find_element(By.XPATH, COST).text
            print(cost)
            current_dict['cost'] = cost
        except:
            print(None)
        try:
            tags = driver.find_element(By.XPATH, TAGS).text
            print(tags)
            current_dict['tags'] = tags
        except:
            print(None)

        restaurant_data.append(current_dict)
    if pg == 0:
        driver.find_element(By.XPATH, '//*[@id="EATERY_LIST_CONTENTS"]/div[2]/div/a').click()
    else:
        driver.find_element(By.XPATH, '//*[@id="EATERY_LIST_CONTENTS"]/div[2]/div/a[2]').click()
    load_page(driver)
pd.DataFrame(restaurant_data).to_csv('Restaurant_data.csv', index=False)

