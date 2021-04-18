import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class TestCheckbox:

    driverpath = '../../driver/chromedriver'
    driver = webdriver.Chrome(executable_path=driverpath)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")


    def test_checkbox(self):
        self.checkboxes = self.driver.find_elements_by_xpath("//input[@type='checkbox']")
        print(len(self.checkboxes))
        for checkbox in self.checkboxes:
            checkbox.click()
            assert checkbox.is_selected()
