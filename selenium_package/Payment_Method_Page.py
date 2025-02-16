from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentMethodPage:
    """this page represent the payment method, how would we like to pay"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def cash_on_delivery(self):
        cash_on_delivery = self.driver.find_element(By.ID,"paymentmethod_0")
        cash_on_delivery.click()

    def pay_in_store(self):
        pay_in_store = self.driver.find_element(By.ID, "paymentmethod_1")
        pay_in_store.click()

    def prepayment(self):
        prepayment = self.driver.find_element(By.ID, "paymentmethod_2")
        prepayment.click()

    def credit_card(self):
        credit_card = self.driver.find_element(By.ID, "paymentmethod_3")
        credit_card.click()

    def wait_for_next_button_3(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "payment-method-next-step-button")))

    def click_next_button_3(self):
        next_button = self.driver.find_element(By.CLASS_NAME,"payment-method-next-step-button")
        next_button.click()