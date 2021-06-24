from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(num):
    return str(math.log(abs(12 * math.sin(int(num)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    ans = browser.find_element_by_id('answer')
    ans.send_keys(y)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
