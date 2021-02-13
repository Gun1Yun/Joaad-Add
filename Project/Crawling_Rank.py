import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


# webdriver option setting
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920X1080")


# shopping url & query
URL = "https://shopping.naver.com/"
query = "주차번호판"
title = "조아애드 풀메탈 듀얼 야광 주차번호판 20여종"

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


# get html information
# print(browser.page_source)

# want to find rank
view_rank = 12
rank = 1
find = False

iter_cnt = view_rank//6 + 1

for _ in range(iter_cnt):
    # scroll down
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

    # bf4 instance
    soup = BeautifulSoup(browser.page_source, "lxml")

    ad_lst = soup.find_all("li", attrs={"class": "basicList_item__2XT81 ad"})

    for ad in ad_lst:
        link_element = ad.find("a", attrs={"class": "basicList_link__1MaTN"})
        link = link_element["href"]
        print(link_element.get_text())

        if title == link_element.get_text():
            print("rank : {}, title : {}".format(
                rank, title
            ))
        rank += 1

    # next page
    next_btn = browser.find_element_by_class_name("pagination_next__1ITTf")
    next_btn.click()
    time.sleep(1)


# phase
while True:
    pass
