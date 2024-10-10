from Data.DataAPI import *
from Data.DataUI import *
import requests
import allure
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPageAPI():
    def __init__(self, baseURL:str) -> None:
        self.baseURL = baseURL

    def add_order(self, product_id:int):
        header = {
            "Authorization": token
            }
        body = {"id":product_id,"adData":{"item_list_name":"bestsellers-page","product_shelf":""}}
        resp =  requests.post(self.baseURL + 'cart/product',headers=header, json=body)
        return resp.status_code
    
    def get_product_list(self):
        header = {
            "Authorization": token
            }
        resp = requests.get(GetProductURL, headers=header)
        return resp.json()
    
    def get_product_id(self) ->int:
        resp = self.get_product_list()['data'][0]['id']
        return int(resp)
    

class MainPageUI():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        
    def get_chitai_gorod(self):
        self.driver.get(URL_UI)
        self.driver.find_element(By.CSS_SELECTOR, 'div div.change-city-container div div.change-city__buttons div.button.change-city__button.change-city__button--accept.blue').click()

        

    def search_book(self, phrase:str):
        self.driver.find_element(By.CSS_SELECTOR, input_locator).send_keys(phrase)    
        WebDriverWait(self.driver, 5,2).until(EC.presence_of_element_located((By.CSS_SELECTOR, search_clear_button_locator)))
        self.driver.find_element(By.CSS_SELECTOR, search_button_locator).click()
        resp = WebDriverWait(self.driver, 5,1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, books_list_locator)))
        return resp
    
    def add_product(self, phrase:str):
        self.search_book(phrase)
        but = self.driver.find_element(By.CSS_SELECTOR, button_click_add_product_locator)
        self.driver.execute_script("window.scrollBy(0, 3100)")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, book_img_locator)))
        but.click()
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,button_click_place_an_order_locator), 'ОФОРМИТЬ'))
        result = self.driver.find_element(By.CSS_SELECTOR, button_click_place_an_order_locator).text
        return result
    