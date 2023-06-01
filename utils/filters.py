import allure
from selenium.webdriver.common.by import By
import datetime


# Checking filters for sorting products
class Filters:
    def __init__(self, driver):
        self.driver = driver

    # Filter by price from low to high
    def filters_price_low_high(self):
        with allure.step("Sorting by price"):

            # Click "Filters" button
            filter = self.driver.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
            filter.click()

            # Click "price(low-high)" button
            filter_price_low_high = self.driver.find_element(By.XPATH, '//option[@value="lohi"]')
            filter_price_low_high.click()

            # Check that the products are sorted by price from lower to higher
            product_elements = self.driver.find_elements(By.CSS_SELECTOR, '.inventory_item_price')
            prices = [float(element.text[1:]) for element in product_elements]
            assert prices[0] < prices[1]
            print("OK! Product filtered from low to high price correctly.")

            # Screenshot filter
            now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
            name_screenshot = 'screenshot_filter_' + now_date + '.png'
            screenshot_path = 'c:\\Users\\liliy\\PycharmProjects\\online_shop_test_ui_automation\\screenshots\\'\
                              + name_screenshot
            self.driver.save_screenshot(screenshot_path)

            # Add Screenshot to Allure Report
            allure.attach.file(screenshot_path, name=name_screenshot,
                               attachment_type=allure.attachment_type.PNG)