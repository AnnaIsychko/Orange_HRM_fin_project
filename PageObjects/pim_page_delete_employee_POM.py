from selenium.webdriver.common.by import By
from Test_locators.test_locators import PimPage_EmployeeList_Locators,MyinfoPage_Locators,Dashboardpage_Locators
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_utilities.customLogger import logGen

class Pimpage_Delete_Actions:
    def __init__(self, driver):
        self.driver = driver
        self.pim_emp_loc_obj = PimPage_EmployeeList_Locators()
        self.myinfo_loc_obj = MyinfoPage_Locators()
        self.dashboard_loc_obj = Dashboardpage_Locators()
        self.wait = WebDriverWait(self.driver, timeout=10)
        self.alert_obj = Alert(self.driver) # created an Alert Object
        self.logs_obj = logGen.logger()

    def pim_click(self):
        """
        Clicking on PIM from the Menu
        :return:
        """
        pim_click_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboard_loc_obj.pim_loc_menu_xpath)))
        pim_click_we.click()
        self.logs_obj.info("Clicked on PIM Menu")
    def employee_pim_search(self):
        """
        Searching an employee by giving input in the text field
        :return:
        """
        employeename_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_emp_loc_obj.empname_loc_textbox_xpath)))
        employeename_we.clear()
        employeename_we.send_keys("Madhu")
        emp_search_we = self.driver.find_element(By.XPATH, self.pim_emp_loc_obj.search_loc_btn_xpath)
        emp_search_we.click()
        # self.driver.implicitly_wait(10)
        self.logs_obj.info("Employee search done")

    def employee_pim_delete_click(self):
        """
        Clicking on DELETE button to delete an Employee
        :return:
        """
        # self.driver.execute_script("window.scrollBy(0, 400);")
        emp_pim_delete_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.pim_emp_loc_obj.delete_loc_btn_xpath)))
        # self.driver.implicitly_wait(10)
        emp_pim_delete_we.click()
        print("DELETE clicked")
        self.logs_obj.info("Delete clicked in POM")
        emp_alert_yes_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_emp_loc_obj.alert_loc_yesbtn_xpath)))
        emp_alert_yes_we.click()
        print("YES button clicked")

        #
        # try:
        #         # Wait for the alert to be present
        #         self.alert = self.wait.until(EC.alert_is_present())
        #
        #         # Switch to the alert
        #         self.alert_obj = self.driver.switch_to.alert
        #         self.logs_obj.info("Switched to Alert Window")
        #
        #         # Get the text of the alert
        #         alert_text = self.alert_obj.text
        #         print("Alert Text:", alert_text)
        #
        #         # Handle the alert
        #         self.alert_obj.accept()
        #
        # except TimeoutException:
        #         print("Alert not found within the specified timeout.")
        #         # Handle this case or raise an exception as needed