from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import NoSuchElementException


def new_jobs():
    try:
        options = Options()
        options.headless = True
        Driver = webdriver.Chrome(options=options,
                                  executable_path=r'C:\Users\laptrade\PycharmProjects\Driver\chromedriver.exe')
        Driver.get("https://www.linkedin.com/jobs/search?keywords=Engineering&location=germany&position=1&pageNum=0")
        print("Headless Chrome Initialized")
        time.sleep(2)
        Result = Driver.find_element_by_xpath("//span[@class='results-context-header__job-count']")
        print("Jobs", Result.text)
        New = Driver.find_element_by_xpath("//span[@class='results-context-header__new-jobs']")
        print("New Jobs", New.text)
    except:
        raise NoSuchElementException("No Element found")


new_jobs()
