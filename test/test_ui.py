from Data.DataAPI import *
from Data.DataUI import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.MainPage import MainPageUI
from Pages.CartPage import CartPageUI
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_UI():
    chrome = webdriver.Chrome()
    MPUI = MainPageUI(chrome)
    CPUI = CartPageUI(chrome)
    chrome.implicitly_wait(20)
        
    def test_get_cart(self):
          self.MPUI.get_chitai_gorod()
          self.CPUI.get_cart()
          resp = self.CPUI.get_cart_name()
          assert resp == "КОРЗИНА"

    def test_get_book_list(self):
        self.MPUI.get_chitai_gorod()
        resp = self.MPUI.search_book("Кольцо")
        self.chrome.quit()
        assert len(resp) == 48

    def test_add_product(self):
        self.MPUI.get_chitai_gorod()
        result = self.MPUI.add_product('Гоголь')
        self.chrome.quit()
        assert result == "ОФОРМИТЬ"

    def test_get_cart_list(self):
        self.MPUI.get_chitai_gorod()
        self.CPUI.get_cart()
        list_before = self.CPUI.get_cart_list()
        self.MPUI.add_product('гоголь')
        self.CPUI.get_cart()
        list_after = self.CPUI.get_cart_list()
        self.chrome.quit()
        assert len(list_before)+1 == len(list_after)

    def test_book_quantity_plus(self):
        self.MPUI.get_chitai_gorod()
        self.MPUI.add_product('Достоевский')
        self.CPUI.get_cart()
        quan_before = self.CPUI.get_quan_book_in_cart()
        self.CPUI.product_quantity_plus()
        quan_after = self.CPUI.get_quan_book_in_cart()
        self.chrome.quit()
        assert quan_before == '1 товар'
        assert quan_after == '2 товара'

    def test_book_quantity_min(self):
        self.MPUI.get_chitai_gorod()
        self.MPUI.add_product('Достоевский')
        self.CPUI.get_cart()
        self.CPUI.product_quantity_plus()
        quan_before = self.CPUI.get_quan_book_in_cart()
        self.CPUI.product_quantity_min()
        quan_after = self.CPUI.get_quan_book_in_cart()
        self.chrome.quit()
        assert quan_before == '2 товара'
        assert quan_after == '1 товар'

    def test_delete_one_book_from_cart(self):
        self.MPUI.get_chitai_gorod()
        self.MPUI.add_product('Достоевский')
        self.CPUI.get_cart()
        resp = self.CPUI.delete_one_book()
        self.chrome.quit()
        assert resp == 'ВЕРНУТЬ В КОРЗИНУ'

    def test_delete_cart(self):
        self.MPUI.get_chitai_gorod()
        self.MPUI.add_product('Достоевский')
        self.CPUI.get_cart()
        self.MPUI.add_product('Чехов')
        self.CPUI.get_cart()
        list_before = self.CPUI.get_cart_list()
        resp = self.CPUI.delete_cart()
        assert len(list_before) == 2
        assert resp == 'ВОССТАНОВИТЬ КОРЗИНУ'

    def test_promoution_page(self):
            self.MPUI.get_chitai_gorod()
            resp = self.MPUI.get_promotion_page()
            assert resp == "АКЦИИ"

    def test_sail_page(self):
         self.MPUI.get_chitai_gorod()
         resp = self.MPUI.get_sail_page()
         assert resp == "РАСПРОДАЖА"

    def test_school_page(self):
        self.MPUI.get_chitai_gorod()
        resp = self.MPUI.get_school_page()
        assert resp == 'УЧЕБНЫЕ ПОСОБИЯ'

    def test_comics_page(self):
        self.MPUI.get_chitai_gorod()
        resp = self.MPUI.get_comics_page()
        assert resp == "НОВИНКИ" 

    def test_collection_page(self):
        self.MPUI.get_chitai_gorod()
        resp = self.MPUI.get_collection_page()
        assert resp == "ЧТО ЕЩЁ ПОЧИТАТЬ?"

    def test_articles_page(self):
        self.MPUI.get_chitai_gorod()
        resp = self.MPUI.get_articles_page()
        assert resp == "АКТУАЛЬНОЕ"

    

    