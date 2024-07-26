from PageObjects.login_page_POM import LoginPage_Actions
from PageObjects.pim_page_delete_employee_POM import  Pimpage_Delete_Actions
from PageObjects.myinfo_page_POM import MyinfoPage_Actions
from Test_utilities.customLogger import logGen
from PageObjects.dashboard_page_POM import DashboardPage_Actions
from time import sleep

class Test_pim_employee_delete:

    def test_pim_search(self,setup_browser):
        """
        Testcase to search for an employee
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        LoginPage_Actions_obj = LoginPage_Actions(self.driver)
        pimpage_actions_obj = Pimpage_Delete_Actions(self.driver)
        dashboard_obj = DashboardPage_Actions(self.driver)
        myinfopage_obj = MyinfoPage_Actions(self.driver)

        LoginPage_Actions_obj.login_to_orangehrm_valid()
        logs_obj.info("successfull Login")
        # sleep(5)

        # Clicking on PIM from Menu
        dashboard_obj.click_pim_menu()

        #Clicking on Employee searchh Text Field and clicking on SEARCH button
        pimpage_actions_obj.employee_pim_search()
        self.driver.implicitly_wait(5)

        #Clicking on DELETE button
        pimpage_actions_obj.employee_pim_delete_click()
        logs_obj.info("Employee DELETE button clicked")
        self.driver.implicitly_wait(5)

        # pimpage_actions_obj.employee_pim_delete_alert_handle()
        # logs_obj.info("Switched to Alert window and OK button clicked to DELETE an Employee")