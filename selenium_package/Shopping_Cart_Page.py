from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartPage:
    """this page represent the shopping cart pop up"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def go_to_cart(self):
        return self.driver.find_element(By.LINK_TEXT,"Go to cart")

    def click_go_to_cart(self): #go to actual cart
        self.go_to_cart().click()

    def go_back_to_home_page(self):
        return self.driver.find_element(By.CLASS_NAME,"img-fluid")

    def click_go_back_to_home_page(self): #go back to home page
        self.go_back_to_home_page().click()

    def name_of_each_product(self):
        return self.driver.find_elements(By.CLASS_NAME,"font-weight-medium")

    def name_product_index(self, index_number):
        product_name = self.name_of_each_product()[index_number]
        return product_name.text

    def price_of_each_product(self):
        return self.driver.find_elements(By.CLASS_NAME,"unit-price")

    def price_product_index(self, index_number):
        product_price_text = self.price_of_each_product()[index_number].text
        stop_index = product_price_text.index(" ")
        return product_price_text[1:stop_index].replace(",","")

    def total_quantity(self):
        total_quantity = self.driver.find_element(By.ID,"cart-tab")
        return total_quantity.find_elements(By.TAG_NAME,"span")[1]

    def wait_until_quantity_is_visible(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart-tab > span.badge.badge-pill.label-cart-amount.badge-warning")))

    def total_quantity_text(self):
        return self.total_quantity().text

    def wait_until_quantity_is_updated(self):
        quantity_before = self.total_quantity_text()
        wait = WebDriverWait(self.driver, 30)
        wait.until(lambda driver: self.total_quantity_text() != quantity_before)

    def quantity_of_each_product(self):
        return self.driver.find_elements(By.NAME,"item.EnteredQuantity")

    def quantity_product_index(self, index_number):
        product_quantity = self.quantity_of_each_product()[index_number]
        return product_quantity.get_attribute("value")

    def remove_product_from_cart(self, index_number):
        product_to_remove = self.driver.find_elements(By.CLASS_NAME,"fa-trash-alt")
        return product_to_remove[index_number]

    def click_remove_product_from_cart(self, index_number): #removing product from the cart
        return self.remove_product_from_cart(index_number).click()

    def wait_until_shopping_cart_window_shown(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "offcanvas-cart")))

    def shopping_cart_titles(self):
        return self.driver.find_elements(By.CLASS_NAME,"title")

    def shopping_cart_random_title_text(self,index_number):
        return self.shopping_cart_titles()[index_number].text

    def close_the_shopping_cart_window(self):
        return self.driver.find_element(By.CLASS_NAME,"canvas-slidable")

    def click_close_the_shopping_cart_window(self):
        self.close_the_shopping_cart_window().click()

    def wait_until_shopping_cart_window_closed(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "canvas-slidable")))


    def sub_total(self):
        return self.driver.find_element(By.CLASS_NAME,"sub-total")

    def sub_total_text(self):
        stop_index = self.sub_total().text.index(" ")
        return self.sub_total().text[1:stop_index].replace(",","")

    def wait_until_sub_total_is_updated(self):
        sub_total_before = self.sub_total_text()
        wait = WebDriverWait(self.driver, 30)
        wait.until(lambda driver: self.sub_total_text() != sub_total_before)

    def no_items_in_the_cart(self):
        return self.driver.find_element(By.CLASS_NAME,"no-item-title")

    def no_items_in_the_cart_text(self):
        return self.no_items_in_the_cart().text



