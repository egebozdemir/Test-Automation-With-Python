from selenium.common import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Facade class to be used at all page objects
class BasePage(object):

    def __init__(self, driver, explicit_wait=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_clickable(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except (NoSuchElementException, ElementClickInterceptedException,
                ElementNotInteractableException, StaleElementReferenceException):
            return False

