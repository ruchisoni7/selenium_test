import time

import pytest
from selenium import webdriver

class TestDropdown:

    driverpath = '../../driver/chromedriver'
    driver = webdriver.Chrome(executable_path=driverpath)
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")


    def test_dropdown(self):
        self.driver.find_element_by_id("autosuggest").send_keys("ind")
        time.sleep(2)
        self.countries = self.driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
        print(len(self.countries))
        for country in self.countries:
            if country.text == "India":
                country.click()
                break

        assert self.driver.find_element_by_id("autosuggest").get_attribute('value') == 'India'


