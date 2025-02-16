from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    """this page represent the home page"""
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def categories(self):
        return self.driver.find_elements(By.CLASS_NAME,"art")

    def category(self, random_index):
        return self.categories()[random_index]

    def click_category(self, random_index): #click on category
        self.category(random_index).click()


    def category_names(self):
        return self.driver.find_elements(By.CLASS_NAME,"art-genericname")

    def category_text(self,random_index):
        return self.category_names()[random_index].text

    def home_welcome_title_name(self):
        home_welcome_name = self.driver.find_element(By.CLASS_NAME,"h2")
        return home_welcome_name.text

    def log_in_icon(self):
        return self.driver.find_element(By.CLASS_NAME,"fa-user-circle")

    def click_log_in_icon(self): #go to log in page
        self.log_in_icon().click()

    def log_out_icon(self):
        return self.driver.find_element(By.CLASS_NAME,"fa-sign-out-alt")

    def click_log_out_icon(self): #log out the user
        self.log_out_icon().click()

    def account_icon_text(self):
        account_icon_text = self.driver.find_element(By.CSS_SELECTOR,"#menubar-my-account > div > a > span")
        return account_icon_text.text

    def user_name_text(self):
        user_name = self.driver.find_element(By.CSS_SELECTOR,"#menubar-my-account > div > a > span")
        return user_name.text

    def shopping_basket_icon(self):
        return self.driver.find_element(By.CLASS_NAME,"icm-bag")

    def click_shopping_basket_icon(self): #open the shopping cart pop up
        self.shopping_basket_icon().click()