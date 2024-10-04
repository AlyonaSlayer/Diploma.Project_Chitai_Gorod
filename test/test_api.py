from Data.DataAPI import *
from Data.DataUI import *
import requests
import allure
from Pages.CartPage import CartPageAPI
from Pages.MainPage import MainPageAPI
class Test_cart():
    CP_api = CartPageAPI(BaseURL)
    MP_api = MainPageAPI(BaseURL)
    def test_get_cart(self):
        resp = self.CP_api.get_cart()
        assert len(resp) > 1
    
    def test_add_order(self):
        cart_before = self.CP_api.get_cart()['products']
        resp = self.MP_api.add_order()
        cart_after = self.CP_api.get_cart()['products']
        self.CP_api.delete_cart()
        assert len(cart_after) == len(cart_before)+1

    def test_put_order_by_cart(self):
        self.MP_api.add_order()
        cart_before = self.CP_api.get_cart()['products']
        order_id= cart_before[0]['id']
        resp = self.CP_api.put_order_by_cart(order_id)
        cart_after = self.CP_api.get_cart()['products']
        self.CP_api.delete_cart()
        assert cart_after[0]['quantity'] == cart_before[0]['quantity']+1

    def test_delete_cart(self):
        cart_before = self.CP_api.get_cart()['products']
        self.CP_api.delete_cart()
        cart_after = self.CP_api.get_cart()['products']
        assert len(cart_before)>len(cart_after)
        assert len(cart_after) == 0