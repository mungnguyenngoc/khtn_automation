import pytest
from selenium import webdriver
from time import sleep
class BaseTest:
    @pytest.fixture(scope= "class", autouse=True)
    def setup_driver(self, request):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://opensource-demo.orangehrmlive.com/")
        sleep(7)
        request.cls.driver = driver
        yield
        driver.quit()