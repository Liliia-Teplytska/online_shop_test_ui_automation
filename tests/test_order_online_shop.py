import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.authorization import Authorization
from utils.filters import Filters
from utils.cart import Cart
from utils.finish_order import FinishOrder
from utils.logger import Logger


# Testing the possibility of placing an order in the online shop
@allure.epic("Testing the possibility of placing an order in the online shop")
class TestOrderOnlineShop():

    @allure.description("Test for authorization, sorting products by price, adding to cart and completing the order")
    def test_order(self):
        # Open browser Chrome
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        browser_Chrome = "Google Chrome 113.0.5672.127"   # log info

        # Open Base URL
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        # Log test information
        Logger.setup_logger()
        Logger.checking(method_name="Authorization", browser_name=browser_Chrome)

        # Correct username and password
        username = "standard_user"
        password = "secret_sauce"

        # Authorization
        auth = Authorization(driver, username, password)
        auth.login()

        # Log test information
        Logger.setup_logger()
        Logger.checking(method_name="Sorting by price", browser_name=browser_Chrome)

        # Filters for sorting products
        filters_products = Filters(driver)
        filters_products.filters_price_low_high()

        # Log test information
        Logger.setup_logger()
        Logger.checking(method_name="Add products to the cart and check", browser_name=browser_Chrome)

        # Adding products to cart
        cart = Cart(driver)
        cart.add_products_to_cart()
        expected_item_names = [item["name"] for item in cart.added_products]
        expected_item_prices = [item["price"] for item in cart.added_products]

        # Log test information
        Logger.setup_logger()
        Logger.checking(method_name="Confirm and complete the order", browser_name=browser_Chrome)

        # Complete the order
        finish = FinishOrder(driver, expected_item_names, expected_item_prices)
        finish.finish_order()

        # Close browser Chrome
        driver.quit()

        print("\nTest of placing the order in the online shop passed successfully!!!")

