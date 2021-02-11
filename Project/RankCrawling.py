import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# shopping url
URL = "https://shopping.naver.com/"
query = "주차번호판"

# Find driver path
DRIVER_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))
DRIVER_PATH = DRIVER_DIR + "\chromedriver.exe"

# browser run
browser = webdriver.Chrome(DRIVER_PATH)
browser.get(URL)

search_elem = browser.find_element_by_name("query")
search_elem.send_keys(query)
search_elem.send_keys(Keys.ENTER)


# scroll down
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# get html information
# print(browser.page_source)

# get rank
ad_lst = browser.find_elements_by_class_name("ad_ad_stk__12U34")
# print(ad_lst)
for ad in ad_lst:
    parent = ad.find_element_by_xpath("../../..")
    element = parent.find_element_by_class_name("basicList_mall__sbVax")
    print(element.text)


# phase
while True:
    pass
