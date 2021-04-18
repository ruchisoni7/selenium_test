
import pytest
from selenium import webdriver


class TestCheckbox:

    driverpath = '../../driver/chromedriver'
    driver = webdriver.Chrome(executable_path=driverpath)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    def test_radiobutton(self):
        self.radiobuttons = self.driver.find_elements_by_xpath("//input[@name='radioButton']")
        self.radiobuttons[2].click()
        assert self.radiobuttons[2].is_selected()