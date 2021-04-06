from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.fastly.com/network-map')
print(driver.title)
# Locators
time.sleep(2)
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tachometer']/div[2]")))

meter = driver.find_element_by_xpath("//*[@id='tachometer']/div[2]")
print("Requests per second", meter.text)

hit = driver.find_element_by_css_selector("div[class='tach-stat hit-ratio flex-col'] div[class='tach-value']")
print("Cache hit ratio", hit.text)

time_hit = driver.find_element_by_css_selector("div[class='tach-stat ttfb flex-col'] div[class='tach-value']")
print("Hit time", time_hit.text)

band = driver.find_element_by_css_selector("div[class='tach-stat bandwidth flex-col'] div:nth-child(1)")
print("Bandwidth", band.text)

driver.close()
driver.quit()
