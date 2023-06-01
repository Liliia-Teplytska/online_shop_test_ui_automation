import allure
from selenium.webdriver.common.by import By
import datetime


# Input customer information, Confirm and Complete the order
class FinishOrder:
    def __init__(self, driver, expected_item_names, expected_item_prices):
        self.driver = driver
        self.expected_item_names = expected_item_names
        self.expected_item_prices = expected_item_prices

    # Continue to place the order
    def finish_order(self):
        with allure.step("Confirm and complete the order"):

            # Scroll down the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Click "Checkout" button
            checkout = self.driver.find_element(By.XPATH, '//button[@id="checkout"]')
            checkout.click()

            # Next page checking by URL
            url = "https://www.saucedemo.com/checkout-step-one.html"
            get_url = self.driver.current_url
            assert url == get_url

            # Input first name, last name, zip code
            first_name = self.driver.find_element(By.XPATH, '//input[@id="first-name"]')
            first_name.send_keys("Alexander")
            last_name = self.driver.find_element(By.XPATH, '//input[@id="last-name"]')
            last_name.send_keys("Ivanov")
            zip_code = self.driver.find_element(By.XPATH, '//input[@id="postal-code"]')
            zip_code.send_keys("61000")

            # Click "Continue" button
            continue_button = self.driver.find_element(By.XPATH, '//input[@id="continue"]')
            continue_button.click()

            # Scroll up the page
            self.driver.execute_script("window.scrollTo(0, 0);")

            # Get a list of products on the order confirmation page
            order_items = self.driver.find_elements(By.CSS_SELECTOR, '.cart_item_label')
            order_item_text = [item.text for item in order_items]

            # Convert list to a string
            order_items_str = ', '.join(order_item_text)

            # Get names of products on the order confirmation page
            cart_item_names = [item.find_element(By.CLASS_NAME, 'inventory_item_name').text
                           for item in order_items]

            # Check if product names match
            assert cart_item_names == self.expected_item_names
            print("OK! Products on the order confirmation page are correct!")

            # Get subtotal sum of the order
            order_subtotal = self.driver.find_element(By.CLASS_NAME, 'summary_subtotal_label').text

            # Check subtotal sum of the order
            numbers_sum_subtotal = [float(price.strip('$')) for price in self.expected_item_prices]
            numbers_order_subtotal = float(order_subtotal.replace('Item total: $', ''))
            summ_subtotal = sum(numbers_sum_subtotal)
            assert summ_subtotal == numbers_order_subtotal
            print("Total sum is $" + str(summ_subtotal))
            print("OK! Total sum of added product is correct!")

            # Screenshot Confirm the order
            now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
            name_screenshot = 'screenshot_confirm_' + now_date + '.png'
            screenshot_path = 'c:\\Users\\liliy\\PycharmProjects\\online_shop_test_ui_automation\\screenshots\\' \
                              + name_screenshot
            self.driver.save_screenshot(screenshot_path)

            # Add Screenshot to Allure Report
            allure.attach.file(screenshot_path, name=name_screenshot,
                               attachment_type=allure.attachment_type.PNG)

            # Click "Finish" button
            finish_button = self.driver.find_element(By.XPATH, '//button[@id="finish"]')
            finish_button.click()

            # Check the completing order by phrase
            text_finish = self.driver.find_element(By.XPATH, '//h2[@class="complete-header"]')
            value_text_finish = text_finish.text
            assert value_text_finish == "Thank you for your order!"
            print("OK! The order is complete!")

            # Screenshot Complete the order
            now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
            name_screenshot = 'screenshot_complete_' + now_date + '.png'
            screenshot_path = 'c:\\Users\\liliy\\PycharmProjects\\online_shop_test_ui_automation\\screenshots\\' \
                              + name_screenshot
            self.driver.save_screenshot(screenshot_path)

            # Add Screenshot to Allure Report
            allure.attach.file(screenshot_path, name=name_screenshot,
                               attachment_type=allure.attachment_type.PNG)