import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Test_data import credentials_valid, credentials_invalid
from Test_locators.test_locators import LoginPage_Locators

# Настройка логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LoginPage_Actions:

    def __init__(self, driver):
        self.login_loc_obj = LoginPage_Locators()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_username_valid_login(self):
        username_we = self.wait.until(EC.element_to_be_clickable((By.NAME, self.login_loc_obj.username_loc_name)))
        username_we.clear()
        username_we.send_keys(credentials_valid.username)
        logging.info("Username entered")

    def enter_password_valid_login(self):
        password_we = self.wait.until(EC.element_to_be_clickable((By.NAME, self.login_loc_obj.password_loc_name)))
        password_we.clear()
        password_we.send_keys(credentials_valid.password)
        logging.info("Password entered")

    def enter_username_invalid_login(self):
        username_we = self.wait.until(EC.element_to_be_clickable((By.NAME, self.login_loc_obj.username_loc_name)))
        username_we.clear()
        username_we.send_keys(credentials_invalid.username)
        logging.info("Invalid username entered")

    def enter_password_invalid_login(self):
        password_we = self.wait.until(EC.element_to_be_clickable((By.NAME, self.login_loc_obj.password_loc_name)))
        password_we.clear()
        password_we.send_keys(credentials_invalid.password)
        logging.info("Invalid password entered")

    def click_login(self):
        login_button_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_loc_obj.login_loc_btn_xpath)))
        login_button_we.click()
        logging.info("Login button clicked")

    def login_to_orangehrm_valid(self):
        self.enter_username_valid_login()
        self.enter_password_valid_login()
        self.click_login()

    def login_to_orangehrm_invalid(self):
        self.enter_username_invalid_login()
        self.enter_password_invalid_login()
        self.click_login()

    def title_of_page(self):
        title_name = self.driver.title
        logging.info(f"Returning title of webpage: {title_name}")
        return title_name

    def dashboard_verify(self):
        try:
            dashboard_verify_we = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.login_loc_obj.dashboard_page)))
            dashboard_text = dashboard_verify_we.text
            logging.info(f"Dashboard text: {dashboard_text}")
            return dashboard_text
        except NoSuchElementException:
            logging.error("Element not found: failed to login")
            return None

    def capture_invalidcredentials(self):
        try:
            capture_invalid_we = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.login_loc_obj.invalid_loc_text_xpath)))
            capture_invalid_text = capture_invalid_we.text
            return capture_invalid_text
        except NoSuchElementException:
            logging.error("Invalid credentials message not found")
            return None

    def login_to_orangehrm(self):
        self.login_to_orangehrm_valid()

    # def capture_screenshot(driver, file_name):
    #     try:
    #         driver.save_screenshot(file_name)
    #         logging.info(f'Screenshot saved as {file_name}')
    #     except Exception as e:
    #         logging.error(f'Failed to capture screenshot: {str(e)}')




#if __name__ == '__main__':
     #LoginPageActions().login_to_orangehrm()