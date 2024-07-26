from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class PimPage_Edit_Actions:

    def __init__(self, driver):
        self.driver = driver

    def pim_click(self):
        """Нажать на меню PIM."""
        pim_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[text()="PIM"]'))
        )
        pim_menu.click()

    def search_user(self, username):
        """Искать пользователя по имени пользователя."""
        search_box = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Type for hints..."]'))
        )
        search_box.send_keys(username)
        search_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        search_button.click()

    def select_random_edit_button(self):
        """Выбрать случайную кнопку РЕДАКТИРОВАТЬ из списка пользователей."""
        edit_buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//button[@class="oxd-icon-button oxd-table-cell-action-space"]'))
        )
        if edit_buttons:
            random_button = random.choice(edit_buttons)
            self.driver.execute_script("arguments[0].scrollIntoView();", random_button)
            random_button.click()
        else:
            raise Exception("Кнопки РЕДАКТИРОВАТЬ не найдены")




