from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


Driver = webdriver.Chrome(ChromeDriverManager().install())
Driver.get("https://www.upwork.com/ab/account-security/login")
Driver.maximize_window()
Login = Driver.find_element_by_id("login_username").send_keys("faizan.berlin@gmail.com")
Continue_btn = Driver.find_element_by_id("login_password_continue").click()
Driver.implicitly_wait(90)
Ps_text = Driver.find_element_by_name("login[password]").click()
Password = Driver.find_element_by_id("login_password").send_keys("reallyawesome123")
Login_btn = Driver.find_element_by_id("login_control_continue").click()
time.sleep(2)
Driver.get("https://www.upwork.com/ab/jobs/search/?sort=recency")
jobs = Driver.find_element_by_class_name("ng-binding")
print(jobs.text)

Driver.close()
Driver.quit()
