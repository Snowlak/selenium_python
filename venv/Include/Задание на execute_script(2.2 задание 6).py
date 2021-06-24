from selenium import webdriver
import time
import math

link = " http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector('.form-group #input_value').text
    res = math.log(abs(12 * math.sin(int(x))))

    inp = browser.find_element_by_id('answer')
    inp.send_keys(str(res))

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element_by_css_selector('button.btn')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
