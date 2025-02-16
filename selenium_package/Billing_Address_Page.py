from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class BillingAddressPage:
    """this page represent the billing address information"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def company(self, company_):
        company = self.driver.find_element(By.ID,"NewAddress_Company")
        company.click()
        company.send_keys(company_)

    def first_name(self, name):
        first_name = self.driver.find_element(By.ID,"NewAddress_FirstName")
        first_name.click()
        first_name.send_keys(name)

    def last_name(self, l_name):
        last_name = self.driver.find_element(By.ID,"NewAddress_LastName")
        last_name.click()
        last_name.send_keys(l_name)

    def address_1(self, address_):
        address_1 = self.driver.find_element(By.ID,"NewAddress_Address1")
        address_1.click()
        address_1.send_keys(address_)

    def address_2(self, second_address):
        address_2 = self.driver.find_element(By.ID,"NewAddress_Address2")
        address_2.click()
        address_2.send_keys(second_address)

    def city(self, city_):
        city = self.driver.find_element(By.ID,"NewAddress_City")
        city.click()
        city.send_keys(city_)

    def zip_code(self, zip_code_):
        zip_code = self.driver.find_element(By.ID,"NewAddress_ZipPostalCode")
        zip_code.click()
        zip_code.send_keys(zip_code_)

    def selections(self):
        return self.driver.find_elements(By.CLASS_NAME,"selection")
    
    def country(self):
        country = self.driver.find_element(By.ID,"select2-NewAddress_CountryId-container")
        country_drop = Select(country)
        country_drop.select_by_visible_text("Germany")
    
    def state(self):
        state = self.selections()[1]
        state_drop = Select(state)
        state_drop.select_by_visible_text("Other Non(US)")

    def phone_number(self, phone_):
        phone_number = self.driver.find_element(By.ID,"NewAddress_PhoneNumber")
        phone_number.click()
        phone_number.send_keys(phone_)

    def wait_for_next_button(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "new-address-next-step-button")))

    def click_next_button(self):
        next_button = self.driver.find_element(By.CLASS_NAME,"new-address-next-step-button")
        next_button.click()



