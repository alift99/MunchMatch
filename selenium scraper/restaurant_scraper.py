from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
import time
import pandas as pd

driver = webdriver.Edge('./msedgedriver.exe')
driver.maximize_window()
driver.get('https://www.tripadvisor.com.sg/Restaurants-g294265-Singapore.html')

df = pd.read_csv('Restaurant_data_filtered.csv').to_dict('records')
output_df = []

for data in df:
    driver.get(data['href'])
    try:
        img_container = driver.find_element(By.XPATH,
                                            '//*[@id="taplc_resp_rr_photo_mosaic_0"]/div[1]/div[1]/div[1]/div[2]/div[2]')
        img_link = img_container.find_element(By.TAG_NAME, 'img').get_attribute('src')
    except:
        img_container = driver.find_element(By.XPATH,
                                            '//*[@id="taplc_resp_rr_photo_mosaic_0"]/div[1]/div[1]/div[1]/div[2]/div[4]')
        img_link = img_container.find_element(By.TAG_NAME, 'img').get_attribute('src')
    rating = driver.find_element(By.CLASS_NAME, 'ZDEqb').text
    n_ratings = driver.find_element(By.CLASS_NAME, 'IcelI').text.split(' ')[0]
    address = driver.find_element(By.CLASS_NAME, 'yEWoV').text
    restaurant_data = {'name': data['name'], 'img_link': img_link, 'rating': rating, 'n_ratings': n_ratings, 'address': address}
    print(restaurant_data)
    output_df.append(restaurant_data)

pd.DataFrame(output_df).to_csv('Restaurant_MetaData.csv', index=False)
