from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class ShoppingCartAfterPage:
    """this page represent the actual shopping cart"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def continue_shopping_button(self):
        return self.driver.find_element(By.NAME,"continueshopping")

    def continue_shopping_button_text(self):
        return self.continue_shopping_button().text

    def sub_total(self):
        return self.driver.find_elements(By.CLASS_NAME,"cart-summary-value")

    def sub_total_text(self):
        return self.sub_total()[3].text[1:].replace(",", "")

    def decrease_product_quantity(self):
        return self.driver.find_elements(By.CLASS_NAME,"fa-minus")

    def click_decrease_product_quantity(self, index_number): #decrease the quantity by 1
        self.decrease_product_quantity()[index_number].click()

    def increase_product_quantity(self):
        return self.driver.find_elements(By.CLASS_NAME,"fa-plus")

    def click_increase_product_quantity(self,index_number): #increase the quantity by 1
        self.increase_product_quantity()[index_number].click()

    def products_prices(self):
        return self.driver.find_elements(By.CLASS_NAME,"price")

    def each_total_product_price_text(self,index_number):
        stop_index = self.products_prices()[index_number].text.index(" ")
        return self.products_prices()[index_number].text[1:stop_index].replace(",","")

    def wait_until_product_1_total_price_updated(self):
        """the initial product 1total price"""
        total_price_before_product_1 = self.each_total_product_price_text(1)
        """wait for the total price of product 1 to be updated"""
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: self.each_total_product_price_text(1) != total_price_before_product_1)

    def wait_until_product_2_total_price_updated(self):
        """the initial product 2 total price"""
        total_price_before_product_2 = self.each_total_product_price_text(3)
        """wait for the total price of product 2 to be updated"""
        wait = WebDriverWait(self.driver, 10)
        wait.until(lambda driver: self.each_total_product_price_text(3) != total_price_before_product_2)

    def fill_boxes(self):
        return self.driver.find_elements(By.CLASS_NAME,"form-control")

    def product_quantity_number(self,index_number):
        quantity = self.fill_boxes()[index_number]
        return quantity.get_attribute("value")

    def checkout_button(self):
        return self.driver.find_element(By.ID,"checkout")

    def click_checkout_button(self): #go to checkout
        self.checkout_button().click()


    def click_home_page_icon(self): #go to home page
        home_page_icon = self.driver.find_element(By.CLASS_NAME,"img-fluid")
        home_page_icon.click()





