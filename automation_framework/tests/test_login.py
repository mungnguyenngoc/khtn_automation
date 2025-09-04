
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium.webdriver.common.by import By
#from .base_test1 import BasTest
from base.base_test import BasTest as BaseTest

class TestOrangeHRM(BaseTest):

    USERNAME_INPUT = (By.NAME,  "username")
    PASSWORD_INPUT = (By.NAME,  "password")
    LOGIN_BUTTON   = (By.CSS_SELECTOR, "button[type='submit']") 
    def test_login(self):
        username = "Admin"
        password = "admin123"
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()