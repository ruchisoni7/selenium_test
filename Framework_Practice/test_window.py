import pytest
from selenium import webdriver


class TestJavaalert:

    driverpath = '../../driver/chromedriver'
    driver = webdriver.Chrome(executable_path=driverpath)
    driver.get("https://the-internet.herokuapp.com/windows")


    def test_window(self):
        self.driver.find_element_by_link_text("Click Here").click()
        childwindow = self.driver.window_handles[1]
        self.driver.switch_to.window(childwindow)
        print(self.driver.find_element_by_tag_name("h3").text)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        print(self.driver.find_element_by_tag_name("h3").text)