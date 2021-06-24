from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_css_selector("h2 #num1").text)
    y = int(browser.find_element_by_css_selector("h2 #num2").text)

    res = str(x + y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(res)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
