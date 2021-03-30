import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Login import login_ad_management

# get id, password
r = open('data.txt', mode='rt', encoding='utf-8')
input_id, input_pw = r.readline().rstrip().split()
r.close()

# == xpath list ==
create_ad_btn_xpath = '//*[@id="root"]/div/div[2]/div/div[4]/div[1]/div/div/div/button'
# first-page-xpath
campaign_type_xpath = {
    'power_link': '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/label',
    'shopping_search': '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/label'
}
campaign_name_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[3]/div[2]/div/input'
no_limit_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[4]/div[2]/div[2]/label'
next_btn_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[2]/button[1]'
# second-page-xpath
md_type_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/label/strong'
dropdown_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/div/button'
no_limit_xpath2 = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div[3]/div[2]/div[3]/div/label/span[2]'
next_btn_xpath2 = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div/div[2]/div[2]/button[2]'
# third-page-xpath
md_id_checkbox_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/label/span'
naver_md_id_radiobtn_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[1]/label[2]/span[2]'
md_id_textbox_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/textarea'
md_search_btn_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[2]/div[4]/div/button'
md_add_btn_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div[3]/div[2]/span/div[1]/div/table/tbody/tr/td[1]/span'
create_ad_last_btn_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div/div/div[2]/div[2]/button[2]'

# login and get driver
browser = login_ad_management(input_id, input_pw)

# use WebDriverWait for find element
wait = WebDriverWait(browser, 10)


def click_element(browser, xpath):
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    browser.execute_script('arguments[0].click()', element)


def create_search(browser, data):
    click_element(browser, create_ad_btn_xpath)

    # == first page ==
    # campaign type = shopping search
    click_element(browser, campaign_type_xpath['shopping_search'])

    # input campagin name
    campaign_name_element = wait.until(
        EC.presence_of_element_located((By.XPATH, campaign_name_xpath)))
    for _ in range(10):
        campaign_name_element.send_keys(Keys.BACK_SPACE)
    time.sleep(0.1)
    campaign_name_element.send_keys(data['advertise_name'])
    campaign_name_element.clear()

    click_element(browser, no_limit_xpath)
    click_element(browser, next_btn_xpath)
    # === second page ===
    click_element(browser, md_type_xpath)
    click_element(browser, dropdown_xpath)

    # find store url & click
    elements = browser.find_elements_by_class_name("dropdown-item")
    for element in elements:
        if element.text == data['shop_mall_address']:
            element.click()
            break
    elements.clear()

    click_element(browser, no_limit_xpath2)
    click_element(browser, next_btn_xpath2)

    # === third page ===
    click_element(browser, md_id_checkbox_xpath)
    click_element(browser, naver_md_id_radiobtn_xpath)

    element = wait.until(EC.presence_of_element_located(
        (By.XPATH, md_id_textbox_xpath)))
    element.send_keys(data['merchandise_id'])
    element.clear()

    click_element(browser, md_search_btn_xpath)
    click_element(browser, md_add_btn_xpath)
    click_element(browser, create_ad_last_btn_xpath)


def main():
    data = {
        'advertise_name': 'test',
        'merchandise_id': 82714587701,
        'shop_mall_address': 'https://smartstore.naver.com/joaad'

    }
    '''
    data
    ----
    campaign name
    md_id  : 82714587701
    shoppinmall address : https://smartstore.naver.com/joaad
    expand letter1
    expand leeter2
    keyword..
    '''
    create_search(browser, data)
    while True:
        pass


if __name__ == "__main__":
    main()
