import sys
sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By  # noqa
from src.PageObject.Locators import GoogleCalcPageLocator  # noqa


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.memory = driver.find_element(By.XPATH, GoogleCalcPageLocator.memory)
        self.result = driver.find_element(By.XPATH, GoogleCalcPageLocator.result)
        self.equal_button = driver.find_element(By.XPATH, GoogleCalcPageLocator.equal_button)
        self.num_buttons = list()
        self.algebraic_buttons = list()  # [/ * - +]
        for i in range(1, 4):
            self.num_buttons.append(driver.find_element(By.XPATH, GoogleCalcPageLocator.num_button.format(i)))
        for i in range(2, 6):
            self.algebraic_buttons.append(driver.find_element(By.XPATH,
                                                              GoogleCalcPageLocator.algebraic_button.format(i)))
