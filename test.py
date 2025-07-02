# import time
#
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# time.sleep(5)
#
# driver.get('https://aningo.ru/calculator/')
#
# time.sleep(5)
#
# top_button = driver.find_element(By.XPATH, '.va-image__content')
#
# top_button.click()
#
# driver.quit()
import time
from pydoc import browse

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input_1 = browser.find_element(By.TAG_NAME, "input")
#     input_1.send_keys("Ivan")
#     input_2 = browser.find_element(By.NAME, "last_name")
#     input_2.send_keys("Petrov")
#     input_3 = browser.find_element(By.CLASS_NAME, "city")
#     input_3.send_keys("Smolensk")
#     input_4 = browser.find_element(By.ID, "country")
#     input_4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# url = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(url)
#     link = browser.find_element(By.LINK_TEXT, "224592")
#     link.click()
#
#     input_1 = browser.find_element(By.TAG_NAME, "input")
#     input_1.send_keys("Ivan")
#     input_2 = browser.find_element(By.NAME, "last_name")
#     input_2.send_keys("Petrov")
#     input_3 = browser.find_element(By.CLASS_NAME, "city")
#     input_3.send_keys("Smolensk")
#     input_4 = browser.find_element(By.ID, "country")
#     input_4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     time.sleep(30)
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/find_xpath_form")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input_fields = browser.find_elements(By.CSS_SELECTOR, "input[required]")
#     for field in input_fields:
#         field.send_keys("Test")
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#     assert len(input_fields) == 3
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(5)
#     # закрываем браузер после всех манипуляций
#     browserfrom selenium import webdriver



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math
#
# url = "https://suninjuly.github.io/get_attribute.html"
# browser = webdriver.Chrome()
# browser.get(url)

# x_value = browser.find_element(By.ID, "input_value")

# def calc(x):
#
#     return str(math.log(abs(12*math.sin(int(x)))))
# x_element = browser.find_element(By., "input_value")
# x = x_element.text
# y = calc(x)

# chest = browser.find_element(By.ID, "treasure")
# valuex = chest.get_attribute("valuex")
# y = calc(valuex)
#
# field = browser.find_element(By.ID, "answer")
# field.send_keys(y)
# checkbox = browser.find_element(By.ID, "robotCheckbox")
# checkbox.click()
# radiobutton = browser.find_element(By.ID, "robotsRule")
# radiobutton.click()
# submit_button = browser.find_element(By.CSS_SELECTOR, "button")
# submit_button.click()
# time.sleep(10)
# browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
# url = "https://suninjuly.github.io/selects1.html"
#
# browser = webdriver.Chrome()
# browser.get(url)
# num_1 = int(browser.find_element(By.ID, "num1").text)
# num_2 = int(browser.find_element(By.ID, "num2").text)
# sum = str(num_2 + num_1)
#
# select = Select(browser.find_element(By.TAG_NAME, "select"))
# select.select_by_value(sum)
# button = browser.find_element(By.TAG_NAME, "button")
# button.click()
#
# time.sleep(6)
# browser.quit()


# x = browser.find_element(By.ID, "input_value").text
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
# y = calc(x)
#
# browser.execute_script("window.scrollBy(0, 100);")
#
# field = browser.find_element(By.ID, "answer")
# field.send_keys(y)
#
# checkbox = browser.find_element(By.ID, "robotCheckbox")
# checkbox.click()
#
# radiobutton = browser.find_element(By.ID, "robotsRule")
# radiobutton.click()
#
# submit = browser.find_element(By.TAG_NAME, "button")
# submit.click()
#
# time.sleep(7)
# browser.quit()
import os


# first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
# last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
# email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
#
# first_name.send_keys("Test")
# last_name.send_keys("Testov")
# email.send_keys("test@mail.ru")
#
# current_dir = os.path.abspath(os.path.dirname(__file__))
# file_path = os.path.join(current_dir, "test.txt")
#
# file = browser.find_element(By.ID, "file")
# file.send_keys(file_path)
#
# submit = browser.find_element(By.TAG_NAME, "button")
# submit.click()


# button = browser.find_element(By.TAG_NAME, "button")
# button.click()
#
# confirm = browser.switch_to.alert
# confirm.accept()
#
# x = browser.find_element(By.ID, "input_value").text
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
# y = calc(x)
#
# input = browser.find_element(By.TAG_NAME, "input")
# input.send_keys(y)
#
# submit = browser.find_element(By.TAG_NAME, "button")
# submit.click()

# url = "https://suninjuly.github.io/redirect_accept.html"
# browser = webdriver.Chrome()
# browser.get(url)
#
# button = browser.find_element(By.TAG_NAME, "button")
# button.click()
#
# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)
#
# x = browser.find_element(By.ID, "input_value").text
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
# y = calc(x)
#
# input = browser.find_element(By.TAG_NAME, "input")
# input.send_keys(y)
#
# submit = browser.find_element(By.TAG_NAME, "button")
# submit.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(1)
browser.get("https://suninjuly.github.io/explicit_wait2.html")

book = browser.find_element(By.ID, "book")
price_100 = WebDriverWait(browser, 5).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100"))
book.click()

x = browser.find_element(By.ID, "input_value").text
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)
field = browser.find_element(By.ID, "answer")
field.send_keys(y)

submit = browser.find_element(By.ID, "solve")
submit.click()

time.sleep(6)
browser.quit()