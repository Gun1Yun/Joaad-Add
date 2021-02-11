import os
from selenium import webdriver

DRIVER_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))
DRIVER_PATH = DRIVER_DIR + "\chromedriver.exe"
# C:\Github\Joaad-Add\chromedriver.exe
browser = webdriver.Chrome(DRIVER_PATH)
browser.get("http://naver.com")
