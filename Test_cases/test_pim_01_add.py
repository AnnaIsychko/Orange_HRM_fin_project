import logging
from PageObjects.login_page_POM import LoginPage_Actions
from PageObjects.myinfo_page_POM import MyinfoPage_Actions
from PageObjects.dashboard_page_POM import DashboardPage_Actions
from PageObjects.pim_page_add_employee_POM import PimAddEmp_Page_Actions
from Test_utilities.customLogger import logGen

class Test_pim_employee_add:

    def test_pim_search(self,setup_browser):
        """
        Testcase to ADD an employee,PIM page
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        loginPage_Actions_obj = LoginPage_Actions(self.driver)
        dashboard_obj = DashboardPage_Actions(self.driver)
        myinfopage_obj = MyinfoPage_Actions(self.driver)
        pim_add_emp_obj = PimAddEmp_Page_Actions(self.driver)

        # Logging into OrangeHRM
        loginPage_Actions_obj.login_to_orangehrm_valid()
        logs_obj.info("successfull Login")
        self.driver.implicitly_wait(5)

        #Clicking on PIM from Menu
        dashboard_obj.click_pim_menu()
        logs_obj.info("PIM clicked")
        self.driver.implicitly_wait(5)

        pim_add_emp_obj.AddEmp()
        logs_obj.info("Add Employee tab clicked on PIM Page")

        pim_add_emp_obj.EnterFirstName_pim("Anya")
        logs_obj.info("Entered FirstName in PIM page")

        pim_add_emp_obj.EnterMiddleName_pim("AAAAAA")
        logs_obj.info("Entered MiddleName in PIM page")

        pim_add_emp_obj.EnterLastName_pim("Student")
        logs_obj.info("Entered LastName in PIM page")

        pim_add_emp_obj.EnterEmpId_pim("09876")
        logs_obj.info("Entered EmployeeID in PIM page")

        pim_add_emp_obj.Savebutton_pim()
        logs_obj.info("Clicked on SAVE button on PIM page")

