from selenium import webdriver
import unittest


def browser_open(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('.first_block .first')
    input1.send_keys('A')
    input2 = browser.find_element_by_css_selector('.first_block .second')
    input2.send_keys('R')
    input3 = browser.find_element_by_css_selector('.first_block .third')
    input3.send_keys('nechto@mail')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text

    browser.quit()
    return welcome_text


class TestSelectors(unittest.TestCase):
    def test_site1(self):
        link = "http://suninjuly.github.io/registration1.html"

        self.assertEqual(browser_open(link), "Congratulations! You have successfully registered!")

    def test_site(self):
        link = "http://suninjuly.github.io/registration2.html"

        self.assertEqual(browser_open(link), "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
