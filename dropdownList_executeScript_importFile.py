from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
import  os

def drobdown_list():
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')
    solution = int(num1.text) + int(num2.text)
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(solution))
    submit_button = browser.find_element_by_css_selector('[type="submit"]')
    submit_button.click()
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

def execute_script_task():
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value")
    x_text = x.text
    y = str(math.log(abs(12*math.sin(int(x_text)))))
    browser.execute_script("window.scrollBy(0, 100);")
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

def import_file():
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("[placeholder='Enter first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[placeholder='Enter last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[placeholder='Enter email']")
    input3.send_keys("iiiii@mail.com")
    element = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
