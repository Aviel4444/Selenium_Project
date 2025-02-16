from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class ShippingAddressPage:
    """this page represent the shipping address information"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def company_1(self, company_):
        company = self.driver.find_element(By.ID,"NewAddress_Company")
        company.click()
        company.send_keys(company_)

    def first_name_1(self, name_):
        first_name = self.driver.find_element(By.ID,"NewAddress_FirstName")
        first_name.click()
        first_name.send_keys(name_)

    def last_name_1(self, last_name_):
        last_name = self.driver.find_element(By.ID,"NewAddress_LastName")
        last_name.click()
        last_name.send_keys(last_name_)

    def address_11(self, address_1_):
        address_1 = self.driver.find_element(By.ID,"NewAddress_Address1")
        address_1.click()
        address_1.send_keys(address_1_)

    def address_21(self, address_2_):
        address_2 = self.driver.find_element(By.ID,"NewAddress_Address2")
        address_2.click()
        address_2.send_keys(address_2_)

    def city_1(self, city_):
        city = self.driver.find_element(By.ID,"NewAddress_City")
        city.click()
        city.send_keys(city_)

    def zip_code_1(self, zip_code_):
        zip_code = self.driver.find_element(By.ID,"NewAddress_ZipPostalCode")
        zip_code.click()
        zip_code.send_keys(zip_code_)

    def selections_1(self):
        return self.driver.find_elements(By.CLASS_NAME,"selection")
    
    def country_1(self):
        country = self.driver.find_element(By.ID,"select2-NewAddress_CountryId-container")
        country_drop = Select(country)
        country_drop.select_by_visible_text("Germany")
    
    def state_1(self):
        state = self.selections_1()[1]
        state_drop = Select(state)
        state_drop.select_by_visible_text("Other Non(US)")

    def phone_number_1(self, phone_):
        phone_number = self.driver.find_element(By.ID,"NewAddress_PhoneNumber")
        phone_number.click()
        phone_number.send_keys(phone_)

    def wait_for_next_button_1(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "new-address-next-step-button")))

    def click_next_button_1(self):
        next_button = self.driver.find_element(By.CLASS_NAME,"new-address-next-step-button")
        next_button.click()