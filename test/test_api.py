from Data.DataAPI import *
from Data.DataUI import *
import allure
from Pages.CartPage import CartPageAPI
from Pages.MainPage import MainPageAPI
class TestAPI():
    CP_api = CartPageAPI(BaseURL)
    MP_api = MainPageAPI(BaseURL)
    def test_get_cart(self):
        resp = self.CP_api.get_cart()
        assert len(resp) >= 0

    def test_get_product_list(self):
        resp = self.MP_api.get_product_list()
        assert len(resp['data']) == 48
    
    def test_get_product_id(self):
        resp = self.MP_api.get_product_id()
        assert resp == 3047107
    
    def test_add_order(self):
        cart_before = self.CP_api.get_cart()
        product_id = self.MP_api.get_product_id()
        self.MP_api.add_order(product_id)
        cart_after = self.CP_api.get_cart()
        self.CP_api.delete_cart()
        assert len(cart_after) == len(cart_before)+1

    def test_put_order_by_cart(self):
        product_id = self.MP_api.get_product_id()
        self.MP_api.add_order(product_id)
        cart_before = self.CP_api.get_cart()
        order_id = cart_before[0]['id']
        self.CP_api.put_product_by_cart(order_id)
        cart_after = self.CP_api.get_cart()
        self.CP_api.delete_cart()
        assert cart_after[0]['quantity'] == cart_before[0]['quantity']+1

    def test_delete_cart(self):
        product_id = self.MP_api.get_product_id()
        self.MP_api.add_order(product_id)
        cart_before = self.CP_api.get_cart()
        self.CP_api.delete_cart()
        cart_after = self.CP_api.get_cart()
        assert len(cart_before)>len(cart_after)
        assert len(cart_after) == 0

    def test_delete_product_by_id(self):
        product_id = self.MP_api.get_product_id()
        self.MP_api.add_order(product_id)
        cart_before = self.CP_api.get_cart()
        order_id = cart_before[0]['id']
        self.CP_api.delete_product_by_id(order_id)
        cart_after = self.CP_api.get_cart()
        self.CP_api.delete_cart()
        assert len(cart_before)-1 == len(cart_after)

    def test_restore_product_after_delete(self):
        product_id = self.MP_api.get_product_id()
        self.MP_api.add_order(product_id)
        order_id = self.CP_api.get_cart()[0]['id']
        self.CP_api.delete_product_by_id(order_id)
        cart_before = self.CP_api.get_cart()
        self.CP_api.product_restore_after_delete(order_id)
        cart_after = self.CP_api.get_cart()
        assert len(cart_before)+1 == len(cart_after)
        assert cart_after[0]['id'] == order_id