from selenium import webdriver
from selenium.webdriver.common.by import By


class OrderDetailsPage:
    """this page represent all the information about our order"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def order_information(self):
        return self.driver.find_elements(By.CLASS_NAME,"text-muted")

    def order_number_1_text(self):
        order_number_1 = self.order_information()[0]
        return order_number_1.text

    def click_home_page_icon(self):
        home_page_icon = self.driver.find_element(By.CLASS_NAME,"img-fluid")
        home_page_icon.click()