import allure
from selenium.webdriver.common.by import By
import datetime


# Adding Two Products to Cart and Checking its Contents
class Cart:
    def __init__(self, driver):
        self.driver = driver
        self.added_products = []  # list of added products

    # Add 2 products to cart: with the lowest price and the 4th one
    def add_products_to_cart(self):
        with allure.step("Add products to the cart and check"):
            # List of products on the  Product Catalog page
            product_elements = self.driver.find_elements(By.CSS_SELECTOR, '.inventory_item')

            # Check that there are at least four products in the list
            assert len(product_elements) >= 4

            # Get the name and price of the 1st product
            first_product_name = product_elements[0].find_element(By.CSS_SELECTOR, '.inventory_item_name').text
            first_product_price = product_elements[0].find_element(By.CSS_SELECTOR, '.inventory_item_price').text

            # Get the name and price of the 4th product
            fourth_product_name = product_elements[3].find_element(By.CSS_SELECTOR, '.inventory_item_name').text
            fourth_product_price = product_elements[3].find_element(By.CSS_SELECTOR, '.inventory_item_price').text

            # Add two product to the cart
            product_elements[0].find_element(By.CSS_SELECTOR, '.btn_inventory').click()
            product_elements[3].find_element(By.CSS_SELECTOR, '.btn_inventory').click()

            # Save name and price of added products
            self.added_products.append({"name": first_product_name, "price": first_product_price})
            self.added_products.append({"name": fourth_product_name, "price": fourth_product_price})
            added_products_str = ', '.join([f"{product['name']} ({product['price']})"
                                            for product in self.added_products])
            print("Added products to cart: " + added_products_str)

            # Click "Cart" button
            cart_products = self.driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
            cart_products.click()

            # Check if the cart is open by URL
            url = "https://www.saucedemo.com/cart.html"
            get_url = self.driver.current_url
            assert url == get_url
            print("OK! Your cart is opened.")

            # Get a list of products in the shopping cart
            cart_items = self.driver.find_elements(By.CSS_SELECTOR, '.cart_item')

            # Check that there are two products in the cart
            assert len(cart_items) == 2

            # Get the names of products in the cart
            cart_item_names = [item.find_element(By.CSS_SELECTOR, '.inventory_item_name').text
                               for item in cart_items]
            cart_item_prices = [item.find_element(By.CSS_SELECTOR, '.inventory_item_price').text
                                for item in cart_items]

            # List of the names of products in the cart
            expected_item_names = [first_product_name, fourth_product_name]

            # Check if product names match
            assert cart_item_names == expected_item_names

            # List of the prices of products in the cart
            expected_item_prices = [first_product_price, fourth_product_price]

            # Check if product prices match
            assert cart_item_prices == expected_item_prices

            # Convert lists to strings
            names_str = ', '.join(cart_item_names)
            prices_str = ', '.join(cart_item_prices)

            print("Name of products in the cart: " + names_str)
            print("Price of products in the cart: " + prices_str)
            print("OK! Your cart is correct.")

            # Screenshot Cart
            now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
            name_screenshot = 'screenshot_cart_' + now_date + '.png'
            screenshot_path = 'c:\\Users\\liliy\\PycharmProjects\\online_shop_test_ui_automation\\screenshots\\' \
                              + name_screenshot
            self.driver.save_screenshot(screenshot_path)

            # Add Screenshot to Allure Report
            allure.attach.file(screenshot_path, name=name_screenshot,
                               attachment_type=allure.attachment_type.PNG)


