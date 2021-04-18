import pytest
from selenium import webdriver

class TestSaleForce:

    driverpath = '../../driver/chromedriver'
    driver = webdriver.Chrome(executable_path=driverpath)
    driver.get("https://login.salesforce.com")

    def test_login(self):
        self.driver.find_element_by_xpath("//input[contains(@class,'username')]").send_keys("ruchi")
        self.driver.find_element_by_css_selector(".password").send_keys("abcd")
        self.driver.find_element_by_link_text("Forgot Your Password?").click()
        self.driver.find_element_by_xpath("//a[text()='Cancel']").click()
        print(self.driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
        #print(self.driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
        print(self.driver.find_element_by_xpath("//form[@name='login']/label").text)






