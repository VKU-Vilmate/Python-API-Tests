from selenium.webdriver.common.by import By


class DjangoLocators:
    LINK = 'https://dev-api-timetracking.vilmate.com'
    EMAIL_INPUT = (By.XPATH, '//input[@name="username"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@type="submit"]')
    USERS_BLOCK = (By.XPATH, '(//a[text()="Users"])[1]')
    DEVELOPER_PROJECTS = (By.XPATH, '//a[text()="Developer projects"]')
    SEARCH_FIELD = (By.XPATH, '//input[@id="searchbar"]')
    SEARCH_BUTTON = (By.XPATH, '//input[@type="submit"]')
    SELECT_PROJECT = (By.XPATH, '(//input[@type="checkbox"])[2]')
    DROPDOWN = (By.XPATH, '//select[@name="action"]')
    DELETE_SELECTED = (By.XPATH, '//option[@value="delete_selected"]')
    EXECUTE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SURE = (By.XPATH, '//input[@type="submit"]')
    ZERO_PROJECTS = (By.XPATH, '//form[@id="changelist-form"]/p')
    DEVELOPER_PROJECT_LINK = (By.XPATH, '//a[text()="Autotest User 1"]')
    DATE_FIELD1 = (By.XPATH, '(//input[@class="vDateField"])[1]')
    DATE_FIELD2 = (By.XPATH, '(//input[@class="vDateField"])[3]')
    DATE_FIELD3 = (By.XPATH, '(//input[@class="vDateField"])[5]')