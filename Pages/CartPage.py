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