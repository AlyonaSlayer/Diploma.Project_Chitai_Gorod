from Data.DataAPI import *
from Data.DataUI import *
import requests
import allure
from selenium.webdriver.common.by import By
from time import sleep
class MainPageAPI():
    def __init__(self, baseURL:str) -> None:
        self.baseURL = baseURL

    def add_order(self):
        header = {
            "Authorization" : token
            }
        body = {"id":7467401,"adData":{"item_list_name":"sales","product_shelf":""}}
        resp =  requests.post(self.baseURL + 'cart/product',headers=header, json=body)
        return resp.status_code
    

class MainPageUI():
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
    
    def search_book(self, phrase:str):
        self.driver.get(URL_UI)
        self.driver.find_element(By.CSS_SELECTOR, input_locators).send_keys(phrase)
        self.driver.find_element.click
        sleep(6)
        self.driver.quit

