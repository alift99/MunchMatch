from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
import time
import pandas as pd

driver = webdriver.Edge('./msedgedriver.exe')
driver.maximize_window()
driver.get('https://www.tripadvisor.com.sg/Restaurants-g294265-Singapore.html')

df = pd.read_csv('Restaurant_data_filtered.csv').to_dict('records')
df = df[397:398]

for data in df:
    driver.get(data['href'])
    if int(driver.find_element(By.XPATH, '//*[@id="REVIEWS"]/div[1]/div/div[1]/span').text.replace("(", "").replace(")", "").replace(",", "")) < 100:
        continue
    collected_reviews = []
    for r_page in range(7):
        collapsed = True
        reviews = driver.find_elements(By.CLASS_NAME, 'review-container')
        for review_element in reviews:
            if review_element.get_attribute('data-collapsed') == 'true' and collapsed: # only uncollapse once
                try:
                    review_element.find_element(By.XPATH, '//*[text()="More"]').click()
                    collapsed = False
                    time.sleep(1)
                    break
                except:
                    pass
        reviews = driver.find_elements(By.CLASS_NAME, 'review-container')
        time.sleep(1)
        for review_element in reviews:
            if len(collected_reviews) == 100:
                break
            current_review = {'topic': review_element.find_element(By.CLASS_NAME, 'noQuotes').text,
                              'review': review_element.find_element(By.CLASS_NAME, 'partial_entry').text}
            print(current_review['topic'])
            collected_reviews.append(current_review)
        try:
            if r_page == 0:
                driver.find_element(By.XPATH, '//*[@id="taplc_location_reviews_list_resp_rr_resp_0"]/div/div[18]/div/div/a[2]').click()
            else:
                driver.find_element(By.XPATH, '//*[@id="taplc_location_reviews_list_resp_rr_resp_0"]/div/div[17]/div/div/a[2]').click()
            time.sleep(3)
        except:
            break
    output = pd.DataFrame(collected_reviews, dtype=str)
    output.to_csv(f'reviews/{data["name"]}.csv', index=False)
    time.sleep(2)

    # '/html/body/div[2]/div[2]/div[2]/div[6]/div/div[1]/div[3]/div/div[5]/div/div[1]/div[2]'
    # '/html/body/div[2]/div[2]/div[2]/div[6]/div/div[1]/div[3]/div/div[5]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div[1]/div[2]/div'
