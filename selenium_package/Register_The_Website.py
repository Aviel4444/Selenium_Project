from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#from selenium.webdriver.common.keys import Keys

class RegisterWebsitePage:
    """this page represent the registration to the website"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def first_name(self):
        first_name = self.driver.find_element(By.ID,"FirstName")
        first_name.click()
        first_name.send_keys("Aviel")

    def last_name(self):
        last_name = self.driver.find_element(By.ID,"LastName")
        last_name.click()
        last_name.send_keys("Eini")

    def date(self):
        return self.driver.find_elements(By.ID,"DateOfBirthDay")

    def day(self):
        day = self.date()[0]
        day_drop = Select(day)
        day_drop.select_by_visible_text("20")

    def month(self):
        month = self.date()[1]
        month_drop = Select(month)
        month_drop.select_by_visible_text("June")

    def year(self):
        year = self.date()[2]
        year_drop = Select(year)
        year_drop.select_by_visible_text("1995")

    def email(self):
        email = self.driver.find_element(By.ID,"Email")
        email.click()
        email.send_keys("aaa123@gmail.com")

    def username(self):
        username = self.driver.find_element(By.ID,"Username")
        username.click()
        username.send_keys("blalala40")

    def password(self):
        password = self.driver.find_element(By.ID,"Password")
        password.click()
        password.send_keys("Aviel40")

    def confirm_password(self):
        confirm_password = self.driver.find_element(By.ID,"ConfirmPassword")
        confirm_password.click()
        confirm_password.send_keys("Aviel40")

    def company_name(self):
        company_name = self.driver.find_element(By.ID,"Company")
        company_name.click()
        company_name.send_keys("Experis")

    def click_register_button(self):
        register_button = self.driver.find_element(By.ID,"register-button")
        register_button.click()

    def click_continue_button(self):
        continue_button = self.driver.find_element(By.LINK_TEXT,"Continue")
        continue_button.click()
