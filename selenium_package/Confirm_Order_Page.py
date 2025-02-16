from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConfirmOrderPage:
    """this page represent the order information and if we confirm it before finish the order"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def agree(self):
        agree = self.driver.find_element(By.ID,"termsofservice")
        agree.click()

    def fill_comment(self):
        comment = self.driver.find_element(By.NAME,"CustomerComment")
        comment.send_keys("Hello Orly, How Are You??")

    def wait_for_confirm_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-buy")))

    def click_confirm_button(self):
        confirm_button = self.driver.find_element(By.CLASS_NAME,"btn-buy")
        confirm_button.click()