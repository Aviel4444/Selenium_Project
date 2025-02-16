from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from random import randint,choice

class SignInPage:
    """this page represent the sign_in page"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def fill_username_email(self):
        username_email = self.driver.find_element(By.ID,"UsernameOrEmail")
        username_email.click()
        username_email.send_keys("blalala40")

    def fill_password(self):
        password = self.driver.find_element(By.ID,"Password")
        password.click()
        password.send_keys("Aviel40")

    def click_remember_me(self):
        remember_me =self.driver.find_element(By.ID,"RememberMe")
        remember_me.click()

    def log_in_fields(self):
        return self.driver.find_elements(By.CLASS_NAME,"form-group")

    def click_log_in(self):
        log_in = self.log_in_fields()[3]
        log_in.click()

    def click_register(self):
        register = self.driver.find_element(By.LINK_TEXT,"Register")
        register.click()