import os
import googletrans
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from url_read import file
import selenium
from selenium.webdriver.common.by import By


PATH = 'C:/Users/DELL/Desktop/project_in/geckodriver.exe'


str = "https://www.amazon.{country}/dp/{asin}"


asin, country = file.get_entry(2)
print(asin, country)

str1 = str.replace("{country}", country)
str2 = str1.replace("{asin}", asin)

# sorry in diffrent languages (for seeing error)
sorry = {'ENTSCHULDIGUNG', 'DÉSOLÉ', 'dispiace'}

# create webdriver object
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(4)

# get website
driver.get(str2)
driver.find_element(By.XPATH, '//*[@id="sp-cc-accept"]').click()

product_id = driver.find_element(By.ID, "productTitle")
print("Product Name : " + product_id.text)

images = driver.find_element(By.TAG_NAME, 'img')
print("Image Link is: " + images.get_attribute('src'))

price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print("Price is : " + price.text)

driver.close()
