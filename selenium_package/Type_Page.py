from selenium import webdriver
from selenium.webdriver.common.by import By


class TypePage:
    """this page represent the page between the home page and the products page"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def types(self):
        return self.driver.find_elements(By.CLASS_NAME, "art")

    def type(self, random_index):
        return self.types()[random_index]

    def click_type(self, random_index): #click on type of products
        self.type(random_index).click()

    def category_name(self):
        category_name = self.driver.find_element(By.CLASS_NAME,"h3")
        return category_name.text

    def product_names(self):
        return self.driver.find_elements(By.CLASS_NAME,"art-genericname")

    def product_name(self,random_index):
        return self.product_names()[random_index].text

    def back_home_page(self):
        return self.driver.find_element(By.CLASS_NAME,"fa-home")

    def click_back_home_page(self): #go back to home page
        self.back_home_page().click()




