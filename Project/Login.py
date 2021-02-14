import os
import time
from selenium import webdriver

url = "https://manage.searchad.naver.com/customers"
login_btn_xpath = '//*[@id="root"]/div/div/div/div/div/div[2]/div/a'
create_ad_btn_xpath = '//*[@id="root"]/div/div[2]/div/div[4]/div[1]/div/div/div/button'

# input by parameter or databases plese delete in this code
input_id = "joaad"
input_pw = "jo022800"


def login_ad_management(id, pw):
    browser = webdriver.Chrome()
    # open manage ad
    browser.get(url)
    time.sleep(0.1)

    # click login btn
    browser.find_element_by_xpath(login_btn_xpath).click()

    # input id & pwd
    browser.find_element_by_name("id").send_keys(input_id)
    browser.find_element_by_name("pw").send_keys(input_pw)
    time.sleep(0.1)
    browser.find_element_by_class_name("btn_login").click()
    time.sleep(1)

    return browser


def main():
    browser = login_ad_management(input_id, input_pw)

    # click create add btn
    browser.find_element_by_xpath(create_ad_btn_xpath).click()
    while True:
        pass


if __name__ == "__main__":
    main()
