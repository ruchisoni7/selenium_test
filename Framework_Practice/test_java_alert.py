import pytest
from selenium import webdriver


class TestJavaalert:

    driverpath = '../../driver/chromedriver'
    driver = webdriver.Chrome(executable_path=driverpath)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    @pytest.mark.skip
    def test_javaalert(self):
        self.validatetext = "option3"
        self.driver.find_element_by_css_selector("input[id='name']").send_keys(self.validatetext)
        self.driver.find_element_by_id('alertbtn').click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        assert self.validatetext in alert_text
        alert.accept()

    def test_javaalert2(self):
        self.validatetext = "option3"
        self.driver.find_element_by_css_selector("input[id='name']").send_keys(self.validatetext)
        self.driver.find_element_by_id("confirmbtn").click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.dismiss()