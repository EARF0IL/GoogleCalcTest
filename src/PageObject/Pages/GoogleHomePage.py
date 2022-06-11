import sys
sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By
from src.PageObject.Locators import GoogleHomePageLocator


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.searching_bar = driver.find_element(By.XPATH, GoogleHomePageLocator.searching_bar)
        self.searching_button = driver.find_element(By.XPATH, GoogleHomePageLocator.searching_button)

