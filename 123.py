from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройте параметры для вашего браузера
options = Options()
options.add_argument("--headless")  # Запуск в фоновом режиме

# Укажите полный путь к вашему драйверу Chrome
service = Service('C:/Users/Admin/.wdm/drivers/chromedriver/win64/126.0.6478.182/chromedriver-win32/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

# Откройте страницу
driver.get("https://opensource-demo.orangehrmlive.com/")

# Ожидание загрузки элементов на странице
wait = WebDriverWait(driver, 10)

try:
    # Войти на сайт
    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username.send_keys("ADMIN")
    password.send_keys("admin123")
    login_button.click()

    # Ожидание загрузки элементов после входа
    pim_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule' and contains(@class, 'oxd-main-menu-item')]")))
    print("Элемент PIM меню найден!")

    # Проверка других элементов
    admin_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule' and contains(@class, 'oxd-main-menu-item')]")))
    print("Элемент Admin меню найден!")

    leave_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/web/index.php/leave/viewLeaveModule' and contains(@class, 'oxd-main-menu-item')]")))
    print("Элемент Leave меню найден!")

except Exception as e:
    print(f"Элемент не найден! Ошибка: {e}")

# Закройте браузер
driver.quit()





