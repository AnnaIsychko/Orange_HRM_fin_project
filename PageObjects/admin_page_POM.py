# PageObjects/admin_page_POM.py

import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Test_locators.test_locators import AdminPage_Locators

# Настройка логирования
logging.basicConfig(level=logging.INFO)

class AdminPage_Actions:

    def __init__(self, driver):
        self.admin_loc_obj = AdminPage_Locators()  # created an object for locator class
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_admin_menu(self):
        """Нажимает на меню Admin."""
        try:
            admin_menu_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.admin_menu_xpath)))
            admin_menu_button.click()
            logging.info("Нажато на элемент меню Admin")
        except Exception as e:
            logging.error(f"Не удалось нажать на элемент меню Admin: {e}")
            raise

    def enter_username_admin(self):
        """Вводит имя пользователя и нажимает на кнопку поиска."""
        try:
            logging.info("Ожидание появления текстового поля имени пользователя")
            username_field = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.admin_loc_obj.username_loc_textbox_xpath)))
            username_field.clear()  # Очищаем поле перед вводом
            username_field.send_keys("Admin")
            logging.info("Введено имя пользователя: Admin")

            # Нажатие кнопки поиска
            logging.info("Ожидание появления кнопки поиска")
            search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.admin_loc_obj.search_btn_xpath)))
            search_button.click()
            logging.info("Нажата кнопка поиска")
        except Exception as e:
            logging.error(f"Не удалось ввести имя пользователя или нажать кнопку поиска: {e}")
            raise

    def get_search_results(self):
        """Получает результаты поиска и возвращает их."""
        try:
            username = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.admin_loc_obj.username_result_xpath))
            ).text
            userrole = self.driver.find_element(By.XPATH, self.admin_loc_obj.userrole_result_xpath).text
            employee_name = self.driver.find_element(By.XPATH, self.admin_loc_obj.employee_name_result_xpath).text
            status = self.driver.find_element(By.XPATH, self.admin_loc_obj.status_result_xpath).text

            logging.info("Получены результаты поиска")
            return username, userrole, employee_name, status
        except Exception as e:
            logging.error(f"Не удалось получить результаты поиска: {e}")
            raise








