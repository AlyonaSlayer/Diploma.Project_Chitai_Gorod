from Data.DataAPI import *
from Data.DataUI import *
import requests
from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPageAPI():
    def __init__(self, baseURL:str) -> None:
        self.baseURL = baseURL
    
    def get_cart(self):
        header= {
            "Authorization" : token
        }
        resp = requests.get(self.baseURL + 'cart',headers=header)
        return resp.json()['products']
    
    def put_product_by_cart(self, id_order:int, quantity:int = 2):
        header = {
            "Authorization" : token
            }
        body = [{"id":id_order,"quantity":quantity}]
        resp =  requests.put(self.baseURL + 'cart',headers=header, json=body)
        return resp.json()
    
    def delete_cart(self):
        header = {
            "Authorization": token
            }
        requests.delete(self.baseURL+ 'cart',headers=header)

    def delete_product_by_id(self, id_order:int):
        header = {
            "Authorization" : token
            }
        resp = requests.delete(self.baseURL + 'cart/product/' + str(id_order), headers=header)

    def product_restore_after_delete(self, product_id:int):
        header = {
            "Authorization" : token
            }
        body = {"productId":product_id}
        resp = requests.post(self.baseURL + 'cart/product-restore', headers=header, json=body)
        return resp.json()
    
class CartPageUI():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def get_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, cart_locator).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'section.cart-sidebar-gift')))

    def product_quantity_plus(self):
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, product_quantity_right_locator).click()
        # WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, cart_number_items), '2 товара'))
        sleep(2)

    def product_quantity_min(self):
        self.driver.find_element(By.CSS_SELECTOR, product_quantity_left_locator).click()
        sleep(2)

    def delete_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, cart_delete_locator).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.button.cart-multiple-delete__button.blue')))
        return self.driver.find_element(By.CSS_SELECTOR, 'div.button.cart-multiple-delete__button.blue').text
        

    def total_sum(self):
        resp = self.driver.find_element(By.CSS_SELECTOR, cart_total_sum_locator)
        return resp
    
    def get_quan_book_in_cart(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, cart_img_book_locator)))
        resp = self.driver.find_element(By.CSS_SELECTOR, cart_number_items).text
        return resp
    
    def get_cart_name(self):
        resp = self.driver.find_element(By.CSS_SELECTOR, cart_name_locator).text
        return resp
    
    def get_cart_list(self):
        resp = self.driver.find_elements(By.CSS_SELECTOR, cart_list_locator)
        return resp
    
    def delete_one_book(self):
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(((By.CSS_SELECTOR, product_delete_by_cart_locator))))
        self.driver.find_element(By.CSS_SELECTOR, product_delete_by_cart_locator).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, product_removed_button_locator)))
        return self.driver.find_element(By.CSS_SELECTOR, product_removed_button_locator).text