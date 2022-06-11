import pytest
from selenium import webdriver
import urllib3


class WebDriverSetup:
    def setup(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
