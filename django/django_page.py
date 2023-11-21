import time

from django.base_page import BasePage
from django.django_locators import DjangoLocators as Locators


class DjangoPage(BasePage):

    def login(self):
        self.element_is_visible(Locators.EMAIL_INPUT).send_keys('admin@vilmate.com')
        time.sleep(0.2)
        self.element_is_visible(Locators.PASSWORD_INPUT).send_keys('admin_admin')
        self.element_is_clickable(Locators.LOGIN_BUTTON).click()

    def open_developer_projects(self):
        self.element_is_clickable(Locators.DEVELOPER_PROJECTS).click()

    def search_project(self):
        self.element_is_visible(Locators.SEARCH_FIELD).send_keys('Autotest User 1')
        self.element_is_clickable(Locators.SEARCH_BUTTON).click()

    def open_project(self):
        self.element_is_clickable(Locators.DEVELOPER_PROJECT_LINK).click()

    def get_date(self):
        field_1 = self.element_is_visible(Locators.DATE_FIELD1).get_attribute('value')
        field_2 = self.element_is_visible(Locators.DATE_FIELD2).get_attribute('value')
        field_3 = self.element_is_visible(Locators.DATE_FIELD3).get_attribute('value')
        day1 = field_1[len(field_1) - 2:]
        day2 = field_2[len(field_2) - 2:]
        day3 = field_3[len(field_3) - 2:]
        return day1, day2, day3

    def delete_project(self):
        self.element_is_visible(Locators.SELECT_PROJECT).click()
        self.element_is_clickable(Locators.DROPDOWN).click()
        self.element_is_visible(Locators.DELETE_SELECTED).click()
        time.sleep(0.2)
        self.element_is_clickable(Locators.EXECUTE_BUTTON).click()
        time.sleep(0.2)
        self.element_is_clickable(Locators.SURE).click()

    def remove_dev_project(self):
        self.login()
        self.open_developer_projects()
        self.search_project()
        self.delete_project()

    def check_dates_and_remove(self):
        self.login()
        self.open_developer_projects()
        self.search_project()
        self.open_project()
        day1, day2, day3 = self.get_date()
        self.driver.back()
        self.delete_project()
        return day1, day2, day3

