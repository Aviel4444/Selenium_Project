from unittest import TestCase
from selenium import webdriver
from time import sleep
from Home_Page import HomePage
from Type_Page import TypePage
from Products_Page import ProductsPage
from Product_Info_Page import ProductInfoPage
from Shopping_Cart_Page import ShoppingCartPage
from Shopping_Cart_after import ShoppingCartAfterPage
from Sign_In_Page import SignInPage
from Billing_Address_Page import BillingAddressPage
from Shipping_Address_Page import ShippingAddressPage
from Shipping_Method_Page import ShippingMethodPage
from Payment_Method_Page import PaymentMethodPage
from Confirm_Order_Page import ConfirmOrderPage
from Order_summary_Page import OrderSummaryPage
from Order_Details_Page import OrderDetailsPage
import logging





class Test(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://bearstore-testsite.smartbear.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.Home_Page = HomePage(self.driver)
        self.type_page = TypePage(self.driver)
        self.products_page = ProductsPage(self.driver)
        self.product_info_page = ProductInfoPage(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)
        self.shopping_cart_after_page = ShoppingCartAfterPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.billing_address_page = BillingAddressPage(self.driver)
        self.shipping_address_page = ShippingAddressPage(self.driver)
        self.shipping_method_page = ShippingMethodPage(self.driver)
        self.payment_method_page = PaymentMethodPage(self.driver)
        self.confirm_order_page = ConfirmOrderPage(self.driver)
        self.order_summary_page = OrderSummaryPage(self.driver)
        self.order_details_page = OrderDetailsPage(self.driver)


    def test_moving_between_pages_on_the_site(self):  #😁
        """in this test we choose a category, and after we choose a type of products we want,
         and also go back to home page and proving that we have been in all the pages we chose"""

        category_name_home_page = self.Home_Page.category_text(1)
        self.Home_Page.click_category(1) #click on category and take the category name in the home page

        self.assertEqual(category_name_home_page, self.type_page.category_name()) #test that shown that we get into the category we chose

        product_name_type_page = self.type_page.product_name(0)
        self.type_page.click_type(0) #click on type and take the type name in the type page

        self.assertEqual(product_name_type_page, self.products_page.product_name()) #test that shown that we get into the type of products we chose

        type_name_back_type_text = self.products_page.go_back_to_type_page_text()
        self.products_page.click_go_back_to_type_page() #click go back to type page and take the product name in the product page

        self.assertEqual(type_name_back_type_text, self.type_page.category_name()) #test that check if we get back to the previous page

        self.type_page.click_back_home_page() #click go back to home page and take the home welcome text in the home page
        home_page_back_home_text = self.Home_Page.home_welcome_title_name()

        self.assertEqual(home_page_back_home_text,"Welcome to our store.") #test that check if we get back to the home page



    def test_total_quantity(self):  #😁
        """in this test we pick 2 different products and add them to the cart,
        we are proving that the total quantity is the sum of the two products each quantity"""

        self.Home_Page.click_category(1) #pick product number 1
        self.type_page.click_type(1)
        self.products_page.click_chosen_product(2)

        self.product_info_page.change_quantity() #change the quantity and add to cart
        self.product_info_page.change_quantity()
        self.product_info_page.click_add_to_cart()

        self.shopping_cart_page.click_go_to_cart() #go to cart and then to home page
        self.shopping_cart_page.click_go_back_to_home_page()

        self.Home_Page.click_category(1) #pick product number 2
        self.type_page.click_type(0)
        self.products_page.click_chosen_product(0)

        self.product_info_page.change_quantity() #change the quantity and add to cart
        self.product_info_page.change_quantity()
        self.product_info_page.change_quantity()
        self.product_info_page.click_add_to_cart()

        sum_quantity = (int(self.shopping_cart_page.quantity_product_index(0)) + #the sum of the quantities
                        int(self.shopping_cart_page.quantity_product_index(1)))

        self.shopping_cart_page.wait_until_quantity_is_visible() #wait until the total quantity is visible

        self.assertEqual(int(self.shopping_cart_page.total_quantity_text()), sum_quantity) #check that the total quantity is true



    def test_details_in_the_shopping_cart(self):  #😁
        """in this test we pick 3 products, add them to the cart and proving that the names,
        prices and quantities are the same as we add"""

        self.Home_Page.click_category(1) #pick product number 1
        self.type_page.click_type(1)
        self.products_page.click_chosen_product(2)

        self.product_info_page.change_quantity() #change the quantity

        product_1_name = self.product_info_page.product_name_text() #giving the name price and quantity of product 1
        product_1_price = self.product_info_page.product_price_quantity_between_2_and_3_text()
        product_1_quantity = self.product_info_page.product_quantity_number()

        self.product_info_page.click_add_to_cart() #add it to cart, go to cart and after to home page
        self.shopping_cart_page.click_go_to_cart()
        self.shopping_cart_page.click_go_back_to_home_page()

        self.Home_Page.click_category(1) #pick product number 2
        self.type_page.click_type(0)
        self.products_page.click_chosen_product(0)

        self.product_info_page.change_quantity() #change the quantity
        self.product_info_page.change_quantity()

        product_2_name = self.product_info_page.product_name_text() #giving the name price and quantity of product 2
        product_2_price = self.product_info_page.product_price_quantity_between_2_and_3_text()
        product_2_quantity = self.product_info_page.product_quantity_number()

        self.product_info_page.click_add_to_cart() #add it to cart, go to cart and after to home page
        self.shopping_cart_page.click_go_to_cart()
        self.shopping_cart_page.click_go_back_to_home_page()

        self.Home_Page.click_category(9) #pick product number 3
        self.type_page.click_type(0)
        self.products_page.click_chosen_product(0)

        self.product_info_page.change_quantity() #change the quantity
        self.product_info_page.change_quantity()
        self.product_info_page.change_quantity()

        product_3_name = self.product_info_page.product_name_text() #giving the name price and quantity of product 3
        product_3_price = self.product_info_page.product_price_quantity_1_text()
        product_3_quantity = self.product_info_page.product_quantity_number()

        self.product_info_page.click_add_to_cart() #add it to cart

        """check that the names in shopping cart are good"""
        self.assertEqual(product_3_name, self.shopping_cart_page.name_product_index(0))
        self.assertEqual(product_2_name, self.shopping_cart_page.name_product_index(1))
        self.assertEqual(product_1_name, self.shopping_cart_page.name_product_index(2))

        """check that the prices in shopping cart are good"""
        self.assertEqual(product_3_price, self.shopping_cart_page.price_product_index(0))
        self.assertEqual(product_2_price, self.shopping_cart_page.price_product_index(1))
        self.assertEqual(product_1_price, self.shopping_cart_page.price_product_index(2))

        """check that the quantities in shopping cart are good"""
        self.assertEqual(product_3_quantity, self.shopping_cart_page.quantity_product_index(0))
        self.assertEqual(product_2_quantity, self.shopping_cart_page.quantity_product_index(1))
        self.assertEqual(product_1_quantity, self.shopping_cart_page.quantity_product_index(2))




    def test_details_updated_after_deletion(self):  #😁
        """in this test we pick 2 products, add them to the cart and remove one of them,
        we are proving that the total quantity and the total price changed due the remove"""

        self.Home_Page.click_category(0) #pick product number 1
        self.type_page.click_type(1)
        self.products_page.click_chosen_product(0)

        self.product_info_page.change_quantity() #change the quantity and add it to cart
        self.product_info_page.change_quantity()
        self.product_info_page.click_add_to_cart()

        self.shopping_cart_page.click_go_to_cart() #go to cart and after to home page
        self.shopping_cart_page.click_go_back_to_home_page()

        self.Home_Page.click_category(0) #pick product number 2
        self.type_page.click_type(0)
        self.products_page.click_chosen_product(3)

        self.product_info_page.change_quantity() #change the quantity and add it to cart
        self.product_info_page.change_quantity()
        self.product_info_page.change_quantity()
        self.product_info_page.click_add_to_cart()

        """the total quantity before remove product"""
        quantity_before_remove = (int(self.shopping_cart_page.quantity_product_index(0)) +
                                  int(self.shopping_cart_page.quantity_product_index(1)))

        """the total quantity after remove product"""
        quantity_after_remove = quantity_before_remove - int(self.shopping_cart_page.quantity_product_index(0))

        """the total price before remove product"""
        total_price_before_remove = (float(self.shopping_cart_page.price_product_index(0)) * float(self.shopping_cart_page.quantity_product_index(0))+
                                     float(self.shopping_cart_page.price_product_index(1)) * float(self.shopping_cart_page.quantity_product_index(1)))

        """the total price after remove product"""
        total_price_after_remove = total_price_before_remove - (float(self.shopping_cart_page.price_product_index(0)) *
                                                                float(self.shopping_cart_page.quantity_product_index(0)))

        self.shopping_cart_page.click_remove_product_from_cart(0) #remove the top product

        self.shopping_cart_page.wait_until_quantity_is_updated() #wait until the total quantity update after removing products

        self.assertEqual(int(self.shopping_cart_page.total_quantity_text()), quantity_after_remove) #check if the total quantity updated after remove one product

        self.shopping_cart_page.wait_until_sub_total_is_updated() #wait until the total price update after removing products

        """check if the total price updated after remove one product"""
        self.assertAlmostEqual(float(self.shopping_cart_page.sub_total_text()), float(total_price_after_remove) , places = 2 )

        """check if the product name still saved after remove one product"""
        self.assertEqual(self.shopping_cart_page.name_product_index(0), self.shopping_cart_page.name_product_index(0))

        """check if the product quantity still saved after remove one product"""
        self.assertEqual(self.shopping_cart_page.quantity_product_index(0), self.shopping_cart_page.quantity_product_index(0))

        """check if the product price still saved after remove one product"""
        self.assertEqual(self.shopping_cart_page.price_product_index(0), self.shopping_cart_page.price_product_index(0))



    def test_open_automatically(self):  #😁
        """in this test we are checking that the shopping cart pop up opens automatically when
        we add products to the cart and also closed automatically, also we check that clicking
        on shopping basket gets us to shopping cart pop up and when clicking go to cart we get
        into the actual cart page"""

        self.Home_Page.click_category(0) #pick product number 1
        self.type_page.click_type(1)
        self.products_page.click_chosen_product(0)

        self.product_info_page.change_quantity() #change the quantity and add it to cart
        self.product_info_page.change_quantity()
        self.product_info_page.click_add_to_cart()

        self.shopping_cart_page.wait_until_shopping_cart_window_shown() #wait until the shopping cart from right opened automatically

        """show that the shopping cart open automatically by see the 'shopping cart' title when click 'add to cart'"""
        self.assertEqual(self.shopping_cart_page.shopping_cart_random_title_text(0),"Shopping Cart")

        self.shopping_cart_page.click_close_the_shopping_cart_window() #closing the shopping cart from right

        self.shopping_cart_page.wait_until_shopping_cart_window_closed() #wait until the shopping cart from right closed automatically

        """show that the shopping cart closed automatically by see the 'add to cart' title when clicking on the background"""
        self.assertEqual(self.product_info_page.add_to_cart().text,"Add to cart")

        self.product_info_page.click_shopping_basket_icon() #click on shopping basket icon

        self.shopping_cart_page.wait_until_shopping_cart_window_shown() #wait until the shopping cart shown after clicking the shopping basket icon

        """show that the shopping cart open automatically by see the 'shopping cart' title when clicking shopping basket icon"""
        self.assertEqual(self.shopping_cart_page.shopping_cart_random_title_text(0), "Shopping Cart")

        self.shopping_cart_page.click_go_to_cart() #go to shopping cart page

        """show that we go to shopping cart page by see continue shopping button when clicking go to cart"""
        self.assertEqual(self.shopping_cart_after_page.continue_shopping_button_text(),"Continue shopping")



    def test_total_price(self):  #😁
        """in this test we pick 3 products, add them to the cart and after go to the actual shopping
        cart, we check that the total price and quantity of each product and the sum prices, quantities
        of all 3 are correct in the pop shopping cart and also in the actual shopping cart"""

        self.Home_Page.click_category(1) #pick product number 1
        self.type_page.click_type(1)
        self.products_page.click_chosen_product(2)

        self.product_info_page.change_quantity() #change the quantity and add it to cart
        self.product_info_page.click_add_to_cart()

        self.shopping_cart_page.click_go_to_cart() #going to shopping cart page and then to home page
        self.shopping_cart_page.click_go_back_to_home_page()

        self.Home_Page.click_category(1) #pick product number 2"
        self.type_page.click_type(0)
        self.products_page.click_chosen_product(0)

        self.product_info_page.change_quantity() #change the quantity and add it to cart
        self.product_info_page.change_quantity()
        self.product_info_page.click_add_to_cart()

        self.shopping_cart_page.click_go_to_cart() #going to shopping cart page and then to home page
        self.shopping_cart_page.click_go_back_to_home_page()

        self.Home_Page.click_category(9) #pick product number 3
        self.type_page.click_type(0)
        self.products_page.click_chosen_product(0)

        self.product_info_page.change_quantity() #change the quantity and add it to cart
        self.product_info_page.change_quantity()
        self.product_info_page.change_quantity()
        self.product_info_page.click_add_to_cart()

        """the total price of all the products"""
        total_price = ((float(self.shopping_cart_page.price_product_index(0)) * int(self.shopping_cart_page.quantity_product_index(0))) +
                       (float(self.shopping_cart_page.price_product_index(1)) * int(self.shopping_cart_page.quantity_product_index(1))) +
                       (float(self.shopping_cart_page.price_product_index(2)) * int(self.shopping_cart_page.quantity_product_index(2))))

        """check that the total sum price of all the prices in the shopping cart before clicking go to cart"""
        self.assertAlmostEqual(float(self.shopping_cart_page.sub_total_text()), total_price, places = 2)

        """print all the products names in the shopping cart"""
        logging.basicConfig(level=logging.INFO)
        logging.info("product number 1 name:" + self.shopping_cart_page.name_product_index(0))
        logging.info("product number 2 name:" + self.shopping_cart_page.name_product_index(1))
        logging.info("product number 3 name:" + self.shopping_cart_page.name_product_index(2))

        """print all the products quantities in the shopping cart"""
        logging.info("product number 1 quantity:" + self.shopping_cart_page.quantity_product_index(0))
        logging.info("product number 2 quantity:" + self.shopping_cart_page.quantity_product_index(1))
        logging.info("product number 3 quantity:" + self.shopping_cart_page.quantity_product_index(2))

        """print all the products prices in the shopping cart"""
        logging.info("product number 1 price:" + self.shopping_cart_page.price_product_index(0) + '$')
        logging.info("product number 2 price:" + self.shopping_cart_page.price_product_index(1) + '$')
        logging.info("product number 3 price:" + self.shopping_cart_page.price_product_index(2) + '$')

        """go to shopping cart page and check that the total sum price of all the prices in the shopping cart after clicking go to cart"""
        self.shopping_cart_page.click_go_to_cart()
        self.assertAlmostEqual(float(self.shopping_cart_after_page.sub_total_text()), total_price)



    def test_total_price_and_quantity_updated_after_changes(self):  #😁
        """in this case we pick 2 products, add them to the cart, going to actual shopping cart
        and change the quantities of two of them, we check that the total price of each product
        changed due the quantities changes and also the sum total changed in the actual shopping
        cart and in the pop shopping cart"""

        self.Home_Page.click_category(0) #pick product number 1
        self.type_page.click_type(1)
        self.products_page.click_chosen_product(0)

        self.product_info_page.change_quantity() #change the quantity and add it to cart
        self.product_info_page.change_quantity()
        self.product_info_page.click_add_to_cart()

        self.shopping_cart_page.click_go_to_cart() #go to shopping cart page and then to home page
        self.shopping_cart_page.click_go_back_to_home_page()

        self.Home_Page.click_category(0) #pick product number 2
        self.type_page.click_type(0)
        self.products_page.click_chosen_product(3)

        self.product_info_page.change_quantity() #change the quantity and add it to cart
        self.product_info_page.change_quantity()
        self.product_info_page.change_quantity()
        self.product_info_page.click_add_to_cart()

        self.shopping_cart_page.click_go_to_cart() #go to shopping cart page

        self.shopping_cart_after_page.click_decrease_product_quantity(0) #decrease the quantity of the first product

        self.shopping_cart_after_page.wait_until_product_1_total_price_updated() #wait until the total price of first product updated after decrease

        self.shopping_cart_after_page.click_decrease_product_quantity(1) #decrease the quantity of the second product

        self.shopping_cart_after_page.wait_until_product_2_total_price_updated() #wait until the total price of second product updated after increase

        """check that the price of product one updated after decrease the quantity"""
        self.assertAlmostEqual(float(self.shopping_cart_after_page.each_total_product_price_text(1)),
                         (float(self.shopping_cart_after_page.product_quantity_number(1)) *
                         float(self.shopping_cart_after_page.each_total_product_price_text(0))))

        """check that the price of product two updated after increase the quantity"""
        self.assertAlmostEqual(float(self.shopping_cart_after_page.each_total_product_price_text(3)),
                         (float(self.shopping_cart_after_page.product_quantity_number(2)) *
                         float(self.shopping_cart_after_page.each_total_product_price_text(2))))

        """giving the sum of prices of all the products"""
        product_1_total_price = float(self.shopping_cart_after_page.each_total_product_price_text(1))
        product_2_total_price = float(self.shopping_cart_after_page.each_total_product_price_text(3))
        total_price = (float(product_1_total_price) + float(product_2_total_price))

        """check that the total price of all the products updated"""
        self.assertEqual(float(self.shopping_cart_after_page.sub_total_text()), float(round(total_price, 10)))

        self.shopping_cart_after_page.click_home_page_icon() #go to home page and open the shopping cart from right
        self.Home_Page.click_shopping_basket_icon()

        """check that the total price of all the products updated in the shipping cart icon from right"""
        self.assertEqual(float(self.shopping_cart_page.sub_total_text()), float(round(total_price, 10)))


    def test_finish_an_order(self):  #😁
        """in this test we pick 2 products, add them to the cart, doing all the process for
        completing an order ,and after we check that the order number is the same as we get,
        also check that our order finally accepted and when we get into the home page our
        shopping cart should be empty"""

        self.Home_Page.click_category(1) #pick product number 1
        self.type_page.click_type(0)
        self.products_page.click_chosen_product(0)

        self.product_info_page.change_quantity() #change the quantity and add it to cart
        self.product_info_page.change_quantity()
        self.product_info_page.click_add_to_cart()

        self.shopping_cart_page.click_go_to_cart() #go to shopping cart page and after to home page
        self.shopping_cart_page.click_go_back_to_home_page()

        self.Home_Page.click_category(9) #pick product number 2
        self.type_page.click_type(0)
        self.products_page.click_chosen_product(0)

        self.product_info_page.change_quantity() #change the quantity and add it to cart
        self.product_info_page.change_quantity()
        self.product_info_page.change_quantity()
        self.product_info_page.click_add_to_cart()

        self.shopping_cart_page.click_go_to_cart() #go to shopping cart page and press on checkout
        self.shopping_cart_after_page.click_checkout_button()

        self.sign_in_page.fill_username_email() #log in an existing account
        self.sign_in_page.fill_password()
        self.sign_in_page.click_log_in()

        self.shopping_cart_after_page.click_checkout_button() #click again the checkout button

        self.billing_address_page.company("hello 12345") #fill all the information in billing address page and press next
        self.billing_address_page.first_name("name")
        self.billing_address_page.last_name("last name")
        self.billing_address_page.address_1("bla1")
        self.billing_address_page.address_2("bla2")
        self.billing_address_page.city("bla3")
        self.billing_address_page.zip_code("0110011")
        #self.billing_address_page.country()
        #self.billing_address_page.state()
        self.billing_address_page.phone_number("1234567891")
        self.billing_address_page.wait_for_next_button()
        self.billing_address_page.click_next_button()

        self.shipping_address_page.company_1("hey you 12345") #fill all the information in shipping address page and press next
        self.shipping_address_page.first_name_1("adi")
        self.shipping_address_page.last_name_1("king")
        self.shipping_address_page.address_11("bla4")
        self.shipping_address_page.address_21("bla5")
        self.shipping_address_page.city_1("bla6")
        self.shipping_address_page.zip_code_1("1001100")
        #self.shipping_address_page.country_1()
        #self.shipping_address_page.state_1()
        self.shipping_address_page.phone_number_1("9876543219")
        self.shipping_address_page.wait_for_next_button_1()
        self.shipping_address_page.click_next_button_1()

        self.shipping_method_page.shop_pickup() #choose shipping method and press next
        self.shipping_method_page.wait_for_next_button_2()
        self.shipping_method_page.click_next_button_2()

        self.payment_method_page.cash_on_delivery() #choose payment method and press next
        self.payment_method_page.wait_for_next_button_3()
        self.payment_method_page.click_next_button_3()

        self.confirm_order_page.agree() #confirm the order information
        self.confirm_order_page.fill_comment()
        self.confirm_order_page.wait_for_confirm_button()
        self.confirm_order_page.click_confirm_button()

        """checks that a message has been received that the order has been accepted"""
        self.assertEqual(self.order_summary_page.order_completed_title_text(),"Your order has been received")

        order_number_in_summary_page = self.order_summary_page.order_number_text() #giving the order number

        self.order_summary_page.wait_for_order_details_button() #wait until order details button us visible and click on it
        self.order_summary_page.click_order_details_button()

        """Checks that the order number we received on 'order summary page'
         matches the order number on 'order details page'"""
        self.assertEqual(order_number_in_summary_page, self.order_details_page.order_number_1_text())

        self.order_details_page.click_home_page_icon() #go to home page and press shopping basket icon to open the shopping cart from right
        self.Home_Page.click_shopping_basket_icon()

        """checks that at the end of the purchase when entering the shopping cart
           we get a message that the shopping cart is empty"""
        self.assertEqual(self.shopping_cart_page.no_items_in_the_cart_text(),"Shopping cart empty")



    def test_log_in_and_log_out(self):  #😁
        """in this test we log into the website with existing account and check that we
        logged in, after we log out and check that we logged out"""

        self.Home_Page.click_log_in_icon() #go to log in page

        self.sign_in_page.fill_username_email() #fill the fields to log in and click log in
        self.sign_in_page.fill_password()
        self.sign_in_page.click_remember_me()
        self.sign_in_page.click_log_in()

        """check that the icon text is now the user name when we logged in"""
        self.assertEqual(self.Home_Page.account_icon_text(),self.Home_Page.user_name_text())

        self.Home_Page.click_log_in_icon() #log out the user
        self.Home_Page.click_log_out_icon()

        """check that the icon text switch to 'log in' when we logged out"""
        self.assertEqual(self.Home_Page.account_icon_text(), "LOG IN")



    def tearDown(self):
        sleep(5)
        self.driver.quit()
