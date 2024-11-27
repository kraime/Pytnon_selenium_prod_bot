import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

my_url = f'https://jivo.chat/OLFhryN3Ur'
option = Options()
option.headless = False
driver = webdriver.Chrome(options=option)
driver.get(my_url)
driver.maximize_window()
time.sleep(5)

with open('questions.json', 'r', encoding="UTF-8") as f:
    data = json.load(f)

for q in data["questions"].values():
    text_input = driver.find_element(By.CLASS_NAME,"inputField__hexqx")
    text_input.click()
    question_value = ActionChains(driver)
    question_value.send_keys(q)
    question_value.perform()
    send_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "sendButton__qKZLo")))
    send_element.click()
    time.sleep(15)

answer_element = driver.find_element(By.CSS_SELECTOR, "body > jdiv > jdiv > jdiv.mobileContainer__OQ6cr.__tablet__tzyZU > jdiv > jdiv:nth-child(2) > jdiv.body__ZoN_w.show__aUaJ7 > jdiv > jdiv > jdiv.scroll__QD0dd > jdiv:nth-child(1)").text

with open('.venv/out.txt', 'w') as output:
    output.write(answer_element)

# print(answer_element)
driver.quit()

