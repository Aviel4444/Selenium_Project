from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderSummaryPage:
    """this page represent the page after confirm the order"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def order_completed_title(self):
        return self.driver.find_element(By.CLASS_NAME,"mt-3")

    def order_completed_title_text(self):
        return self.order_completed_title().text

    def order_number_text(self):
        order_number = self.driver.find_element(By.CSS_SELECTOR,"#content-center > div > div.page-body.checkout-data.pt-4 > div > div > p > a > strong")
        return order_number.text

    def wait_for_order_details_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn-warning")))

    def click_order_details_button(self):
        order_details_button = self.driver.find_element(By.CLASS_NAME,"btn-warning")
        order_details_button.click()

