from selenium.webdriver.common.by import By

class LogoutPage_Actions:
    def __init__(self, driver):
        self.driver = driver

    # Locator for the profile dropdown
    profile_dropdown_xpath = '//span[@class="oxd-userdropdown-tab"]'
    # Locator for the logout button in the dropdown
    logout_button_xpath = '//a[text()="Logout"]'

    def click_profile_dropdown(self):
        self.driver.find_element(By.XPATH, self.profile_dropdown_xpath).click()

    def click_logout_button(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()

    def logout(self):
        self.click_profile_dropdown()
        self.click_logout_button()
