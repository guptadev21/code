import os
from selenium import webdriver

from url_read import file
import selenium
from selenium.webdriver.common.by import By
import json

""" 
Geckodriver is used as web driver for firefox, 
if you want to use chrome or chromium you can visit internet 
and download respective drivers and change location.
""" 

# Specify the path of geckodriver.exe

PATH = 'C:/project_in/geckodriver.exe'

# dictionary object to store respective output
d = {}

for i in range (101):
    url = "https://www.amazon.{country}/dp/{asin}"


    try:
        asin, country = file.get_entry(i)
        country = country.replace("\n", "")
    except Exception:
        continue

    str1 = url.replace("{country}", country)
    str2 = str1.replace("{asin}", asin)



    # create webdriver object
    driver = webdriver.Firefox(executable_path=PATH)

    # get website
    driver.get(str2)

    try:
        driver.find_element(By.XPATH, '//*[@id="sp-cc-accept"]').click()
    
    except Exception:
        d[i] = [str2 + " not available."]

    try:

        temp = []
        product_id = driver.find_element(By.ID, "productTitle")
        temp.append(product_id.text)

        images = driver.find_element(By.TAG_NAME, 'img')
        temp.append(images.get_attribute('src'))

        price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
        price_frac = driver.find_element(By.CLASS_NAME, "a-price-fraction")
        temp.append(price_whole.text + "." + price_frac.text)

        desc = driver.find_element(By.CLASS_NAME, "a-list-item")
        temp.append(desc.text)

        d[i] = temp

    except (Exception):
        driver.close()
        continue

    driver.close()

print(d)
with open("dictionary", "w") as f:
    json.dump(d, f, indent=4, sort_keys=True)


