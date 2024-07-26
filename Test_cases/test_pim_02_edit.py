import pytest
from PageObjects.login_page_POM import LoginPage_Actions
from PageObjects.pim_page_edit_employee_POM import PimPage_Edit_Actions
from Test_utilities.customLogger import logGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class TestPimEmployeeEdit:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        """
        Automatically called before each test function.
        This sets up the browser instance and makes it available as self.driver.
        """
        self.driver = browser

    def test_select_user_and_edit(self):
        """
        Test case for selecting a user from existing users and clicking the Edit button.
        """
        logs_obj = logGen.logger()
        LoginPage_Actions_obj = LoginPage_Actions(self.driver)
        pimpage_actions_obj = PimPage_Edit_Actions(self.driver)

        # Login to the system
        LoginPage_Actions_obj.login_to_orangehrm_valid()
        logs_obj.info("Successfully logged in")

        # Click on PIM menu
        pimpage_actions_obj.pim_click()
        logs_obj.info("PIM menu clicked")

        # Wait for the user list to be visible and then scroll to the list
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//table[@class="oxd-table"]'))
        )

        # Scroll down to ensure the table is fully loaded
        table_element = self.driver.find_element(By.XPATH, '//table[@class="oxd-table"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", table_element)
        logs_obj.info("Scrolled to the user list table")

        # Select a user and click the Edit button
        try:
            # Get all edit buttons
            edit_buttons = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//button[@class="oxd-icon-button oxd-table-cell-action-space"]'))
            )

            if edit_buttons:
                # Randomly select an edit button
                random_button = random.choice(edit_buttons)
                self.driver.execute_script("arguments[0].scrollIntoView();", random_button)
                random_button.click()
                logs_obj.info("Clicked Edit button for a selected user")

                # Perform any additional actions or assertions after clicking Edit
                # For example, you might want to check if the edit page has opened correctly
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//form[@id="editForm"]'))  # Adjust the XPath to match your form
                )
                logs_obj.info("Edit page is visible")
            else:
                logs_obj.error("No edit buttons found")
                assert False, "No edit buttons found"

        except Exception as e:
            logs_obj.error(f"An error occurred: {e}")
            assert False, f"An error occurred: {e}"









