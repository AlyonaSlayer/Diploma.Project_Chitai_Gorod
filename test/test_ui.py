from Data.DataAPI import *
from Data.DataUI import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.MainPage import MainPageUI
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_UI():
    chrome = webdriver.C
    chrome.implicitly_wait(20)
    
    def test_search_book(self):
            self.chrome.get(URL_UI)
            self.chrome.find_element(By.CSS_SELECTOR, input_locators).send_keys("Python")
            self.chrome.find_element(By.CSS_SELECTOR, 'div.header-search__head button').click
            resp = self.chrome.find_elements(By.CSS_SELECTOR, 'div.product-title__author')
            self.chrome.quit()
            assert resp[0] == []