from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShippingMethodPage:
    """this page represent the shipping method"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def shop_pickup(self):
        in_shop_pickup = self.driver.find_element(By.ID,"shippingoption_0")
        in_shop_pickup.click()

    def By_Ground(self):
        by_ground = self.driver.find_element(By.ID,"shippingoption_1")
        by_ground.click()

    def wait_for_next_button_2(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shipping-method-next-step-button")))

    def click_next_button_2(self):
        next_button = self.driver.find_element(By.CLASS_NAME,"shipping-method-next-step-button")
        next_button.click()
