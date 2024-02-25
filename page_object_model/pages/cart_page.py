from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page_object_model.base.base_page import BasePage


class CartPage(BasePage):

    checkout_button = (By.ID, 'checkout')
    remove_item_button = 'remove-sauce-labs-{}'
    item_name = (By.CLASS_NAME, 'inventory_item_name')

    def __init__(self, driver):
        super().__init__(driver)

    def wait_page_load(self):
        self.wait.until(EC.visibility_of_element_located(self.checkout_button))
        self.wait.until(EC.visibility_of_element_located(self.item_name))

    def click_checkout_button(self):
        self.driver.find_element(*self.checkout_button).click()

    def click_remove_item_button(self, product_name):
        self.driver.find_element(By.ID, self.remove_item_button.format(product_name)).click()

    def get_item_name(self):
        return self.driver.find_element(*self.item_name).text

    def remove_item(self, name):
        if self.is_element_clickable((By.ID, self.remove_item_button.format(name))):
            self.click_remove_item_button(name)

    def is_product_removed(self, name):
        return not self.is_element_present((By.ID, self.remove_item_button.format(name)))


