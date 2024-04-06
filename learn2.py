from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.fjlabs.com/portfolio')
#driver.get('https://www.selenium.dev/selenium/web/web-form.html')

#off for try/finally= title = driver.find_element(By.CLASS_NAME,"tag").text

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tag"))
    )
    title = driver.find_element(By.CLASS_NAME,"tag").text
finally:
    print(title)

driver.close()

#exited
