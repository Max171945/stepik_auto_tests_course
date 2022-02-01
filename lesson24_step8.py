from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import MySeleniumUtil

login = input("Enter username: ")
password = input("Enter password: ")
step = "https://stepik.org/lesson/181384/step/8?auth=login&unit=156009"

try:

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    condition = EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 15).until(condition)
    button.click()
    
    answer = MySeleniumUtil.get_answer(browser)
    MySeleniumUtil.send_answer(browser, step, answer, login, password)

finally:

	browser.quit()
    
    



