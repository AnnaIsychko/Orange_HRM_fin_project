from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_locators.test_locators import PimAddEmployee_Locators
from time import sleep
class PimAddEmp_Page_Actions:
    def __init__(self, driver):
        self.driver = driver
        self.pim_addemp_loc_obj = PimAddEmployee_Locators()
        self.wait = WebDriverWait(self.driver,timeout=10)

    def AddEmp(self):
        """
        Clicking on ADD Employee tab on the PIM page
        :return:
        """
        sleep(5)
        addemp_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.pim_addemp_loc_obj.addemp_loc_tab_xpath)))
        addemp_we.click()

    def EnterFirstName_pim(self, firstname):
        """
        Enter FirstName of an Employee
        :return:
        """
        fname_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.pim_addemp_loc_obj.fname_loc_text_xpath)))
        fname_we.clear()
        fname_we.send_keys(firstname)

    def EnterMiddleName_pim(self, middlename):
        """
        Enter Middlename of an Employee
        :return:
        """
        fname_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_addemp_loc_obj.midname_loc_text_xpath)))
        fname_we.clear()
        fname_we.send_keys(middlename)

    def EnterLastName_pim(self, lastname):
        """
        Enter LasttName of an Employee
        :return:
        """
        fname_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_addemp_loc_obj.lastname_loc_text_xpath)))
        fname_we.clear()
        fname_we.send_keys(lastname)

    def EnterEmpId_pim(self, empid):
        """
        Enter Employee ID of an Employee
        :return:
        """
        fname_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_addemp_loc_obj.empid_loc_text_xpath)))
        fname_we.clear()
        fname_we.send_keys(empid)

    def Savebutton_pim(self):
        """
        Click on SAVE button to add an Employee
        :return:
        """
        fname_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_addemp_loc_obj.save_loc_btn_xpath)))
        fname_we.click()