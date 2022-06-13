import sys
sys.path.append(sys.path[0] + "/..")

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.GoogleCalcPage import CalcPage
from src.PageObject.Pages.GoogleHomePage import HomePage
import pytest
from selenium import webdriver


class TestGoogleCalcPage(WebDriverSetup):
    def test_calc_page(self):
        self.driver.get("http://google.com")
        self.driver.set_page_load_timeout(30)

        assert self.driver.title == "Google"

        home_page = HomePage(self.driver)
        home_page.searching_bar.send_keys("Калькулятор")
        home_page.searching_button.click()

        assert self.driver.title == "Калькулятор - Поиск в Google"

        calc_page = CalcPage(self.driver)
        calc_page.num_buttons[0].click()
        calc_page.algebraic_buttons[1].click()
        calc_page.num_buttons[1].click()
        calc_page.algebraic_buttons[2].click()
        calc_page.num_buttons[2].click()
        calc_page.algebraic_buttons[3].click()
        calc_page.num_buttons[0].click()
        calc_page.equal_button.click()

        current_memory = calc_page.memory.text
        current_result = calc_page.result.text

        assert current_memory == "1 × 2 - 3 + 1 ="
        assert current_result == '0'
