import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import datetime
from utils.logger import Logger


# Authorization and Access to the Product Catalog
class Authorization:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    # Authorization
    def login(self):
        with allure.step("Authorization"):

            # Input incorrect username
            username_input = self.driver.find_element(By.ID, "user-name")
            username_input.send_keys(self.username)
            username_input.send_keys(Keys.BACKSPACE)

            # Input correct username
            password_input = self.driver.find_element(By.ID, "password")
            password_input.send_keys(self.password)

            # Click "Login" button
            login_button = self.driver.find_element(By.ID, "login-button")
            login_button.click()

            # Checking Error message
            error_message = self.driver.find_element(By.XPATH, '//h3[@data-test="error"]')
            value_error_message = error_message.text
            search_word = "Epic sadface"
            if search_word in value_error_message:
                print("\nOK! Incorrect login: message about failed login is present.")
            else:
                print("Failed!")

            # Refresh the authorization page
            self.driver.refresh()

            # Input correct username
            username_input = self.driver.find_element(By.ID, "user-name")
            username_input.send_keys(self.username)

            # Input correct password
            password_input = self.driver.find_element(By.ID, "password")
            password_input.send_keys(self.password)

            # Click "Login" button
            login_button = self.driver.find_element(By.ID, "login-button")
            login_button.click()

            # Checking access to the Product Catalog by the word "Products"
            text_products = self.driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')
            value_text_products = text_products.text
            assert value_text_products == "Products"

            # Checking access to the Product Catalog by URL
            url = "https://www.saucedemo.com/inventory.html"
            get_url = self.driver.current_url
            assert url == get_url
            print("OK! Correct login and password: authorization was successful.")

            # Screenshot auth
            now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
            name_screenshot = 'screenshot_auth_' + now_date + '.png'
            screenshot_path = 'c:\\Users\\liliy\\PycharmProjects\\online_shop_test_ui_automation\\screenshots\\' \
                              + name_screenshot
            self.driver.save_screenshot(screenshot_path)

            # Add Screenshot to Allure Report
            allure.attach.file(screenshot_path, name=name_screenshot,
                               attachment_type=allure.attachment_type.PNG)

