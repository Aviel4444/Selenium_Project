from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductsPage:
    """this page represent the products page"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def products(self):
        return self.driver.find_elements(By.CLASS_NAME,"art")

    def chosen_product(self, random_index):
        return self.products()[random_index]

    def click_chosen_product(self, random_index): #click on chosen product
        self.chosen_product(random_index).click()

    def product_name(self):
        product_name = self.driver.find_element(By.CLASS_NAME,"h3")
        return product_name.text


    def go_back_options(self):
        return self.driver.find_elements(By.CLASS_NAME,"breadcrumb-item")

    def go_back_to_type_page_text(self):
        return self.go_back_options()[1].text

    def click_go_back_to_type_page(self): #back to type page the sub category page before the home page
        go_back = self.go_back_options()[1]
        go_back.click()
