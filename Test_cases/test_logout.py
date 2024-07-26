import logging
from PageObjects.login_page_POM import LoginPage_Actions
from PageObjects.dashboard_page_POM import DashboardPage_Actions
from PageObjects.logout_page_POM import LogoutPage_Actions
from Test_utilities.customLogger import logGen

class Test_logout:

    def test_logout(self, setup_browser):
        """
        Testcase to Logout from OrangeHRM
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        loginPage_Actions_obj = LoginPage_Actions(self.driver)
        dashboard_obj = DashboardPage_Actions(self.driver)
        logoutPage_Actions_obj = LogoutPage_Actions(self.driver)

        try:
            # Logging into OrangeHRM
            loginPage_Actions_obj.login_to_orangehrm_valid()
            logs_obj.info("Successfully logged in to OrangeHRM")
            self.driver.implicitly_wait(5)

            # Clicking on PIM from Menu (or navigate as needed)
            dashboard_obj.click_pim_menu()
            logs_obj.info("Clicked on PIM menu")

            # Performing Logout
            logoutPage_Actions_obj.logout()
            logs_obj.info("Clicked on Logout button")

            # Verifying logout (this may involve checking if login page is displayed)
            # Assuming we are redirected to the login page after logout
            assert self.driver.title == "OrangeHRM"  # Adjust according to the actual title of the login page
            logs_obj.info("Successfully logged out and redirected to login page")

        except Exception as e:
            logs_obj.error(f"Test failed due to: {str(e)}")
            raise
