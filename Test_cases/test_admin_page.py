import pytest
import time
from PageObjects.login_page_POM import LoginPage_Actions
from PageObjects.admin_page_POM import AdminPage_Actions
from Test_utilities.customLogger import logGen

class Test_AdminPage:

    def test_click_on_admin(self, setup_browser):
        """
        Test for clicking the Admin menu item and performing search actions
        :param setup_browser: fixture for setting up the browser
        :return: None
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        LoginPage_Actions_obj = LoginPage_Actions(driver=setup_browser)
        AdminPage_Actions_obj = AdminPage_Actions(driver=setup_browser)

        # Login to the application
        LoginPage_Actions_obj.login_to_orangehrm()

        # Logging and performing actions on the Admin page
        logs_obj.info("Clicking on the Admin menu item")
        AdminPage_Actions_obj.click_admin_menu()

        logs_obj.info("Entering username")
        AdminPage_Actions_obj.enter_username_admin()

        logs_obj.info("Waiting for search results to load")
        time.sleep(3)  # Replace with a more appropriate wait if needed

        logs_obj.info("Getting search results")
        username, userrole, employee_name, status = AdminPage_Actions_obj.get_search_results()

        # Log and print search results
        logs_obj.info(f"Search results: username={username}, userrole={userrole}, employee_name={employee_name}, status={status}")

        print(f"Username: {username}")
        print(f"User Role: {userrole}")
        print(f"Employee Name: {employee_name}")
        print(f"Status: {status}")

        # Additional checks for search results can be added here












