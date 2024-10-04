from Data.DataAPI import *
from Data.DataUI import *
from selenium import webdriver
from selenium.webdriver.common.by import By
driver_chrome = webdriver.Chrome()
from Pages.MainPage import MainPageUI
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_UI():
    driver_chrome = webdriver.Chrome()
    
    
    def test_search_book(self):
            self.driver_chrome.get(URL_UI)
            self.driver_chrome.find_element(By.CSS_SELECTOR, input_locators).send_keys("Корнишон")
            self.driver_chrome.find_element(By.CSS_SELECTOR, '.button').click
            sleep(6)
            self.driver_chrome.quit()
            assert 1==1