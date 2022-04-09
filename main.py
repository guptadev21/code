from multiprocessing.connection import wait
from selenium import webdriver
from url_read import file
import time

str = "https://www.amazon.{country}/dp/{asin}"
asin, country = file.get_entry(0)
print(asin, country)

str1 = str.replace("{country}", country)
str2 = str1.replace("{asin}", asin)
# create webdriver object
driver = webdriver.Firefox()
# get google.co.in
driver.get(str2)
time.sleep(3)
driver.close()
