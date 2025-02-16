from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductInfoPage:
    """this page represent the product information"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def quantity(self):
        return self.driver.find_element(By.CLASS_NAME,"fa-plus")

    def clear_quantity_box(self):
        self.quantity().clear()

    def change_quantity(self): #change the quantity by adding 1
        self.quantity().click()

    def add_to_cart(self):
        return self.driver.find_element(By.LINK_TEXT,"Add to cart")

    def click_add_to_cart(self): #add the product to the cart
        self.add_to_cart().click()

    def product_name(self):
        return self.driver.find_element(By.CLASS_NAME,"pd-name")

    def product_name_text(self):
        return self.product_name().text

    def product_quantity_number(self):
        product_quantity = self.driver.find_element(By.CLASS_NAME,"form-control-lg")
        return product_quantity.get_attribute("value")

    def product_price_1_quantity(self):
        return self.driver.find_element(By.CLASS_NAME,"pd-price")

    def product_price_quantity_1_text(self): #the price of product with quantity 1
        stop_index = self.product_price_1_quantity().text.index(" ")
        return self.product_price_1_quantity().text[1:stop_index].replace(",","")

    def product_price_quantity_above_1_quantity(self):
        return self.driver.find_elements(By.CLASS_NAME,"pd-tierprice-price")

    def product_price_quantity_between_2_and_3_text(self): #the price of product with quantity 2-3
        return self.product_price_quantity_above_1_quantity()[0].text[1:].replace(",","")

    def product_price_quantity_between_4_and_5_text(self): #the price of product with quantity 4-5
        return self.product_price_quantity_above_1_quantity()[1].text[1:].replace(",", "")

    def icons(self):
        return self.driver.find_elements(By.CLASS_NAME,"navbar-toggler")

    def click_shopping_basket_icon(self): #open the shopping cart pop up
        shopping_cart_icon = self.icons()[2]
        shopping_cart_icon.click()



