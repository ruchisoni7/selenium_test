import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWait:

    driverpath = '../../driver/chromedriver'
    driver = webdriver.Chrome(executable_path=driverpath)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


    def test_wait(self):
        #self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector(".search-keyword").send_keys("ber")
        time.sleep(2)
        count = self.driver.find_elements_by_xpath('//div[@class="products"]/div')
        #assert count == 3
        buttons = self.driver.find_elements_by_css_selector("div[class='product-action'] button")
        for button in buttons:
            button.click()
        self.driver.find_element_by_css_selector('img[alt="Cart"]').click()
        self.driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
        self.driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
        self.driver.find_element_by_css_selector(".promoBtn").click()
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
        print(self.driver.find_element_by_css_selector(".promoInfo").text)




