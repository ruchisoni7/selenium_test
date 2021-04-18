import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class TestLocators:
    driverpath = '../../driver/chromedriver'
    driver = webdriver.Chrome(executable_path=driverpath)
    driver.get("https://rahulshettyacademy.com/angularpractice/")


    @pytest.mark.skip
    def test_verify_title(self):
        title = self.driver.title
        print(f"Received Title : {title}")
        assert title == 'ProtoCommerce'

    #@pytest.mark.skip
    def test_formsubmission(self):
        #self.driver.find_element_by_name("name").send_keys("Ruchi")
        self.driver.find_element_by_css_selector("input[name='name']").send_keys("ruchi")
        self.driver.find_element_by_name("email").send_keys("ruchi@gmail.com")
        self.driver.find_element_by_css_selector("input[type='password']").send_keys("Colt")
        self.driver.find_element_by_id("exampleCheck1").click()

        dropdown = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        dropdown.select_by_visible_text("Female")
        dropdown.select_by_index(0)
        #dropdown.select_by_value("")
        self.driver.find_element_by_xpath("//input[@value='Submit']").click()
        message = self.driver.find_element_by_class_name('alert-success').text
        print(len(message))
        print('1st',message[0], message[1])
        message_expected_output = "Success! The Form has been submitted successfully!."
        assert message_expected_output in message






    #def test_HTML_locator(self):
      #  TestLocators.Setup()




