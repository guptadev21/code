import os
import googletrans
from selenium import webdriver

from url_read import file
import selenium
from selenium.webdriver.common.by import By


PATH = 'C:/project_in/geckodriver.exe'

for i in range (10):
    url = "https://www.amazon.{country}/dp/{asin}"


    asin, country = file.get_entry(i)
    print("Entry number " + str(i) + ": ", asin, country)

    str1 = url.replace("{country}", country)
    str2 = str1.replace("{asin}", asin)



    # create webdriver object
    driver = webdriver.Firefox(executable_path=PATH)
    #driver.implicitly_wait(4)

    # get website
    driver.get(str2)

    try:
        driver.find_element(By.XPATH, '//*[@id="sp-cc-accept"]').click()
    
    except Exception:
        print(str2 + "not available.")

    try:

        product_id = driver.find_element(By.ID, "productTitle")
        print("Product Name : " + product_id.text)

        images = driver.find_element(By.TAG_NAME, 'img')
        print("Image Link is: \n" + images.get_attribute('src'))

        price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
        price_frac = driver.find_element(By.CLASS_NAME, "a-price-fraction")
        print("Price is : " + price_whole.text + "." + price_frac.text)

        desc = driver.find_element(By.CLASS_NAME, "a-list-item")
        print("About the item :\n" + desc.text)

    except (Exception):
        print(Exception)

    driver.close()
