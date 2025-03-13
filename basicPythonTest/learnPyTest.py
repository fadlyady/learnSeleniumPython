from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("http://www.google.com")
print(driver.title)
searchBox = driver.find_element(By.NAME, "q")
searchBox.send_keys("Python" + Keys.ENTER)
time.sleep(5)
driver.quit()