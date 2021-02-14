import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Login import login_ad_management


create_ad_btn_xpath = '//*[@id="root"]/div/div[2]/div/div[4]/div[1]/div/div/div/button'
campaign_type_xpath = {
    'power_link': '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/label',
    'shopping_search': '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/label'
}
campaign_name_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div/input'
no_limit_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[4]/div[2]/div[2]/label/span[2]'
next_btn_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[2]/button[1]'
md_type_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/label/strong'
dropdown_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/div/button'
no_limit_xpath2 = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div[3]/div[2]/div[3]/div/label/span[2]'
next_btn_xpath2 = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div[2]/button[2]'
# guide
#browser = webdriver.Chrome()
##

browser = login_ad_management(input_id, input_pw)


def create_search(broswer, data):
    browser.find_element_by_xpath(create_ad_btn_xpath).click()
    time.sleep(1)

    # campaign type = shopping search
    browser.find_element_by_xpath(
        campaign_type_xpath['shopping_search']).click()

    # input campagin name
    campaign_name_element = browser.find_element_by_xpath(campaign_name_xpath)
    for _ in range(10):
        campaign_name_element.send_keys(Keys.BACK_SPACE)
    time.sleep(0.1)
    campaign_name_element.send_keys("campaign_name")
    campaign_name_element.clear()

    # no limit budget
    browser.find_element_by_xpath(no_limit_xpath).click()
    # go to next page
    browser.find_element_by_xpath(next_btn_xpath).click()
    time.sleep(0.1)

    # === second page ===
    browser.find_element_by_xpath(md_type_xpath).click()
    time.sleep(0.1)
    browser.find_element_by_xpath(dropdown_xpath).click()

    # find store url & click
    elements = browser.find_elements_by_class_name("dropdown-item")
    for element in elements:
        if element.text == 'https://smartstore.naver.com/joaad':
            element.click()
            print('find!')
            break
    elements.clear()

    browser.find_element_by_xpath(no_limit_xpath2).click()
    browser.find_element_by_xpath(next_btn_xpath2).click()
    time.sleep(0.1)

    # === third page ===


def main():
    data = 1
    '''
    data
    ----
    campaign name
    md_id
    shoppinmall address
    expand letter1
    expand leeter2
    keyword..
    '''
    create_search(browser, data)
    while True:
        pass


if __name__ == "__main__":
    main()
