from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute("valuex")
    y = calc(x)

    ans = browser.find_element_by_id('answer')
    ans.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
