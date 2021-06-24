from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_name('firstname')
    name.send_keys('a')

    surname = browser.find_element_by_name('lastname')
    surname.send_keys('s')

    email = browser.find_element_by_name('email')
    email.send_keys('nechto@mail')

    # получаем путь к директории текущего исполняемого файла
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(curr_dir, 'nechto.txt')

    file_button = browser.find_element_by_id('file')
    file_button.send_keys(file_path)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
