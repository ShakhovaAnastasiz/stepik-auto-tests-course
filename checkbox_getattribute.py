from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def checkbox_test():
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    checkbox_robbot = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox_robbot.click()
    radio_robots = browser.find_element_by_css_selector('[value="robots"]')
    radio_robots.click()
    submit_button = browser.find_element_by_css_selector('[type="submit"]')
    submit_button.click()
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
def get_attribute_task():
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x_value = x_element.get_attribute('valuex')
    y = calc(x_value)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    checkbox_robbot = browser.find_element_by_id('robotCheckbox')
    checkbox_robbot.click()
    radio_robots = browser.find_element_by_css_selector('[value="robots"]')
    radio_robots.click()
    submit_button = browser.find_element_by_css_selector('[type="submit"]')
    submit_button.click()
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

