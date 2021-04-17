from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def jobs():
    try:
        options = Options()
        options.headless = True
        Driver = webdriver.Chrome(options=options,
                                  executable_path=r'C:\Users\laptrade\PycharmProjects\Driver\chromedriver.exe')
        Driver.get("https://www.upwork.com/ab/account-security/login")
        print("Headless Chrome Initialized")
        time.sleep(5)
        Driver.save_screenshot("after.png")
        Login = WebDriverWait(Driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='login_username']]"))).click()
        Driver.save_screenshot("before.png")
        # Login = Driver.find_element_by_css_selector("#login_username")
        # Login.click()
        Login.send_keys("faizan.berlin@gmail.com")
        Continue_btn = Driver.find_element_by_id("login_password_continue")
        Continue_btn.click()
        Driver.implicitly_wait(90)
        Ps_text = Driver.find_element_by_name("login[password]")
        Ps_text.click()
        Password = Driver.find_element_by_id("login_password")
        Password.click()
        Password.send_keys("reallyawesome123")
        Login_btn = Driver.find_element_by_id("login_control_continue")
        Login_btn.click()
        time.sleep(2)
        Driver.get("https://www.upwork.com/ab/jobs/search/?sort=recency")
        jobs_count = Driver.find_element_by_class_name("ng-binding")
        print(jobs_count.text)
        Driver.close()
        Driver.quit()
    except:
        raise NoSuchElementException("No Element found")


jobs()
