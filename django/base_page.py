from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def refresh(self):
        self.driver.refresh()

    def element_is_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

