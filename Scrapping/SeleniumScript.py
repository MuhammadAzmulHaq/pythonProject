from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def fast():
    options = Options()
    options.headless = True
    # Locators
    Driver = webdriver.Chrome(options=options,
                              executable_path=r'C:\Users\laptrade\PycharmProjects\Driver\chromedriver.exe')
    # wait = WebDriverWait(driver, 10)
    # element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tachometer']/div[2]")))
    Driver.get('https://www.fastly.com/network-map')
    print(Driver.title)
    time.sleep(2)
    meter = Driver.find_element_by_xpath("//*[@id='tachometer']/div[2]")
    print("Requests per second", meter.text)

    hit = Driver.find_element_by_css_selector("div[class='tach-stat hit-ratio flex-col'] div[class='tach-value']")
    print("Cache hit ratio", hit.text)

    time_hit = Driver.find_element_by_css_selector("div[class='tach-stat ttfb flex-col'] div[class='tach-value']")
    print("Hit time", time_hit.text)

    band = Driver.find_element_by_css_selector("div[class='tach-stat bandwidth flex-col'] div:nth-child(1)")
    print("Bandwidth", band.text)

    Driver.close()
    Driver.quit()


fast()
