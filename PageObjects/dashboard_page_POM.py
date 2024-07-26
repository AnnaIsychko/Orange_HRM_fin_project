from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_locators.test_locators import Dashboardpage_Locators
import logging
from Test_utilities.customLogger import logGen
class DashboardPage_Actions:
    def __init__(self,driver):

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.dashboard_loc_obj = Dashboardpage_Locators()
        self.logs_obj = logGen.logger()
    def click_pim_menu(self):
        """
        Click on PIM Menu
        :return:
        """
        pim_menu_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboard_loc_obj.pim_loc_menu_xpath)))
        pim_menu_we.click()
        self.logs_obj.info("PIM clicked on POM class")