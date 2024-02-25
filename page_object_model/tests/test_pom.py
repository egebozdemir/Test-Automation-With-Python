import time

from selenium.webdriver.common.by import By

from page_object_model.base.base_test import BaseTest
from page_object_model.pages.login_page import LoginPage


class TestPom(BaseTest):

    driver = 'chrome'

    def test_pom(self):
        login = LoginPage(self.driver)
        login.enter_user_name('standard_user')
        login.enter_password('secret_sauce')
        home_page = login.click_login_button()
        time.sleep(5)
        name = home_page.get_product_name()
        #home_page.click_add_to_cart_backpack()  # specific add_to_cart for 'backpack' product
        home_page.click_add_to_cart('backpack')  # generic add_to_cart by passing product name
        cart = home_page.click_cart_button()
        cart_name = cart.get_item_name()
        self.assertEqual(name, cart_name, 'Product is not added to cart')
        cart.remove_item('backpack')
        self.assertTrue(cart.is_product_removed('backpack'))
        time.sleep(10)