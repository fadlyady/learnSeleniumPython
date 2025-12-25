from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

username = "standard_user"
password = "secret_sauce"

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
print(driver.title)

# get locator for login page
field_username = driver.find_element(By.ID, "user-name")
field_password = driver.find_element(By.ID, "password")
button_login = driver.find_element(By.ID, "login-button")

field_username.send_keys(username)
field_password.send_keys(password)
button_login.click()

#validate success login
shoppping_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
if shoppping_cart.is_displayed():
    print("Login success")
else:
    print("Login failed")

assert shoppping_cart.is_displayed()

time.sleep(5)
driver.quit()