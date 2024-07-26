import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from Test_locators.test_locators import MyinfoPage_Locators
from time import sleep
class MyinfoPage_Actions:
    def __init__(self,driver):
        self.driver = driver
        self.myinfo_loc_obj = MyinfoPage_Locators()
        self.action_obj = ActionChains(driver) # Creating an ActionChain object using webdriver instance
        self.wait = WebDriverWait(self.driver, timeout=10)

    def EnterFirstName_myinfo(self,f_name):
        """
        Enter FirstName of an Employee
        :return:
        """
        firstname_we = self.wait.until(EC.element_to_be_clickable((By.NAME, self.myinfo_loc_obj.firstname_loc_text_name)))
        # firstname_we.clear() # This clear() method was NOT working
        # # Clear the field using JavaScript,this method was also not working,so tried with keyboard keys
        # # self.driver.execute_script("arguments[0].value = '';", fullname_we)

        # Clear the existing value using keyboard shortcuts (Ctrl+A followed by Delete)
        firstname_we.send_keys(Keys.CONTROL + 'a')
        firstname_we.send_keys(Keys.DELETE)
        firstname_we.send_keys(f_name)
        sleep(3)

    def EnterMiddleName_myinfo(self, mname):
        """
        Enter MiddleName of an Employee
        :return:
        """
        middlename_we = self.wait.until(EC.element_to_be_clickable((By.NAME, self.myinfo_loc_obj.middlename_loc_text_name)))
        middlename_we.send_keys(Keys.CONTROL + 'a')
        middlename_we.send_keys(Keys.DELETE)
        middlename_we.send_keys(mname)

    def EnterLastName_myinfo(self, lname):
        """
        Enter LastName of an Employee
        :return:
        """
        lastname_we = self.wait.until(EC.element_to_be_clickable((By.NAME, self.myinfo_loc_obj.lastname_loc_text_name)))
        sleep(2)
        lastname_we.send_keys(Keys.CONTROL + 'a')
        lastname_we.send_keys(Keys.DELETE)
        lastname_we.send_keys(lname)

    def EnterNickName_myinfo(self, nname):
        """
        Enter NickName of an Employee
        :return:
        """
        nickname_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.nickname_loc_text_xpath)))
        nickname_we.send_keys(Keys.CONTROL + 'a')
        nickname_we.send_keys(Keys.DELETE)
        nickname_we.send_keys(nname)

    def EnterEmpID_myinfo(self, empid):
        """
        Enter Employee ID of an Employee
        :return:
        """
        empid_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.empid_loc_text_xpath)))
        empid_we.send_keys(Keys.CONTROL + 'a')
        empid_we.send_keys(Keys.DELETE)
        empid_we.send_keys(empid)

    def EnterOtherID_myinfo(self, otherid):
        """
        Enter Other ID of an Employee
        :return:
        """
        otherid_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.otherid_loc_text_xpath)))
        otherid_we.send_keys(Keys.CONTROL + 'a')
        otherid_we.send_keys(Keys.DELETE)
        otherid_we.send_keys(otherid)

    def EnterDriverLicense_myinfo(self, lic_num):
        """
        Enter Driver License of an Employee
        :return:
        """
        licnum_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.driverlicense_loc_text_xpath)))
        licnum_we.send_keys(Keys.CONTROL + 'a')
        licnum_we.send_keys(Keys.DELETE)
        licnum_we.send_keys(lic_num)

    def EnterLicenseExpiry_myinfo(self, lic_exp):
        """
        Enter License Expity of an Employee
        :return:
        """
        licexp_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.liceexpiry_loc_cal_xpath)))
        licexp_we.send_keys(Keys.CONTROL + 'a')
        licexp_we.send_keys(Keys.DELETE)
        licexp_we.send_keys(lic_exp)

    def EnterSsnNum_myinfo(self, ssn_num):
        """
        Enter SSN Number of an Employee
        :return:
        """
        ssn_num_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.ssnnum_loc_text_xpath)))
        ssn_num_we.send_keys(Keys.CONTROL + 'a')
        ssn_num_we.send_keys(Keys.DELETE)
        ssn_num_we.send_keys(ssn_num)

    def EnterSinNum_myinfo(self, sin_num):
        """
        Enter SIN Number of an Employee
        :return:
        """
        sin_num_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.sinnum_loc_text_xpath)))
        sin_num_we.send_keys(Keys.CONTROL + 'a')
        sin_num_we.send_keys(Keys.DELETE)
        sin_num_we.send_keys(sin_num)

    # def EnterNationality(self, nationality):
    #     nation_we = self.driver.find_element(By.XPATH, self.myinfo_loc_obj.nationality_loc_ddown_xpath)
    #     select_obj = Select(nation_we) # Select object created for the drop-down element
    #     select_obj.select_by_visible_text(nationality) #Accessing methods of the select class

    def EnterNationality_myinfo(self):
        """
        Enter Nationality of an Employee
        :return:
        """
        nation_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.nationality_loc_ddown_xpath)))
        nation_we.click() #clicking on the dropdown arrow
        nation_select_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.myinfo_loc_obj.nationality_loc_selectcountry_xpath))) # choosing the country
        self.action_obj.move_to_element(nation_select_we).click(nation_select_we).perform()

    def EnterMarital_myinfo(self):
        """
        Enter Marital status of an Employee
        :return:
        """
        marital_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.marital_loc_ddown_xpath)))
        marital_we.click() #clicking on the dropdown arrow
        marital_select_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.myinfo_loc_obj.marital_loc_select_xpath))) # choosing the marital
        self.action_obj.move_to_element(marital_select_we).click(marital_select_we).perform()

    def EnterDOB_myinfo(self, dob):
        """
        Enter DOB of an Employee
        :return:
        """
        dob_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.dob_loc_cal_xpath)))
        dob_we.send_keys(Keys.CONTROL + 'a')
        dob_we.send_keys(Keys.DELETE)
        dob_we.send_keys(dob)

    def EnterGender_myinfo(self):
        """
        Enter Gender of an Employee
        :return:
        """
        gender_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.gender_loc_xpath)))
        gender_we.click()

    def EnterMilitary_myinfo(self,milit):
        """
        Enter Military of an Employee
        :return:
        """
        milit_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.military_loc_text_xpath)))
        milit_we.send_keys(Keys.CONTROL + 'a')
        milit_we.send_keys(Keys.DELETE)
        milit_we.send_keys(milit)

    def ClickOnSave_myinfo(self):
        """
        Click in SAVE button
        :return:
        """
        save_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.save_personal_btn_loc_xpath)))
        save_we.click()

    def BloodType_myinfo(self):
        """
        Select Blood Type from the dropdown
        :return:
        """
        blood_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.myinfo_loc_obj.blood_loc_ddown_xpath)))
        blood_we.click()
        action_obj = ActionChains(self.driver)
        blood_select_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.blood_loc_selecttype_xpath)))
        action_obj.move_to_element(blood_select_we).click(blood_select_we).perform()

    def ClickOnSave_custom(self):
        """
        Click on SAVE button in the Customs Field
        :return:
        """
        save_custom_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.savecustom_loc_btn_xpath)))
        save_custom_we.click()

    # def AttachmentsAdd_myinfo(self):
    #     """
    #     Click on ADD button
    #     :return:
    #     """
    #     attachadd_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.myinfo_loc_obj.attachadd_loc_btn_xpath))) #Browse button
    #     attachadd_we.click()
    #
    #     # Wait for the native file dialog to open
    #     sleep(5)  # Adjust the delay as needed
    #
    #     # Simulate typing the file path using PyAutoGUI
    #     file_path = 'C:/Users/madhu/PycharmProjects/OrangeHRM_Guvi_ATProject_1/Test_data.jpg'
    #     pyautogui.write(file_path)
    #     print("wrote filepath")
    #     sleep(4)
    #     pyautogui.press('enter')
    #     print("Enter pressed")
    #     sleep(5)
    #
    #     attachsave_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.myinfo_loc_obj.attachsave_loc_btn_xpath)))
    #     attachsave_we.click()


    def update_field(self, field_name, value):
            """Обновить конкретное поле на странице редактирования."""
            field_locator = (By.NAME, field_name)
            field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(field_locator)
            )
            field.clear()
            field.send_keys(value)

    def save_changes(self):
            """Нажать на кнопку Сохранить на странице редактирования."""
            save_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
            save_button.click()