from Data.DataAPI import *
from Data.DataUI import *
import requests
import allure

class CartPageAPI():
    def __init__(self, baseURL:str) -> None:
        self.baseURL = baseURL
    
    def get_cart(self):
        header= {
            "Authorization" : token
        }
        resp = requests.get(self.baseURL + 'cart',headers=header)
        return resp.json()
    
    def put_order_by_cart(self, id_order:int):
        header = {
            "Authorization" : token
            }
        body = [{"id":id_order,"quantity":2}]
        resp =  requests.put(self.baseURL + 'cart',headers=header, json=body)
        return resp.json()
    
    def delete_cart(self):
        header = {
            "Authorization" : token
            }
        requests.delete(self.baseURL+ 'cart',headers=header)
    

class CartPageUI():
    def put_order_by_cart(self):
        resp