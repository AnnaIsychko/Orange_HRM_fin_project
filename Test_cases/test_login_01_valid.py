from selenium.webdriver.support.ui import WebDriverWait
from PageObjects.login_page_POM import LoginPage_Actions
from Test_utilities.customLogger import logGen

class TestLoginPage:
    def test_login_page_valid(self, setup_browser):  # Pass the 'setup_browser' fixture as an argument
        """
        Testcase for Valid Login - Positive Testcase
        :return:
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        LoginPage_Actions_obj = LoginPage_Actions(driver=setup_browser)  # Create an instance of orangehrm_LoginPageActions class

        logs_obj.info("Starting the Test")
        LoginPage_Actions_obj.login_to_orangehrm_valid()  # Call the method on the instance

        dashboard_text = LoginPage_Actions_obj.dashboard_verify()

        dashboard_page = 'Dashboard'
        if dashboard_page == dashboard_text:
             logs_obj.info("************** Login Successfull,Im in Dashboard Page ****************")
             print("****************** Login Successfull,Im in Dashboard Page *************")
             logs_obj.info("*** Login Test Passed ***")
             logs_obj.info("Test Completed")
             self.driver.close()

        else:
            logs_obj.info("Login Failed,Invalid credentials")
            print("Login Failed")
            self.driver.save_screenshot("../Screenshots/Login_Failed.png")
            logs_obj.info("Test Completed")
            self.driver.close()

