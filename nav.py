from selenium import webdriver
from selenium.webdriver.common.by import By
from config import EMAIL, PASSWORD
import time


# Navigate to the webpage
driver = webdriver.Chrome()
driver.get('https://collective2.com/')

# Find/click login button
try:
    button = driver.find_element(By.XPATH, '//*[@id="home"]/div[1]/nav/div/div[2]/div/a[1]')
    button.click()

except Exception as e:
    print(f'An error occurred {e}')

# Find email field, insert email
try:
    email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    email_field.send_keys(EMAIL)

except Exception as e:
    print(f'An error occurred {e}')

# Find password field, insert password
try:
    email_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    email_field.send_keys(PASSWORD)

except Exception as e:
    print(f'An error occurred {e}')


# Find/click Login button
try:
    button = driver.find_element(By.XPATH, '//*[@id="doLoginCorp"]')
    button.click()

except Exception as e:
    print(f'An error occurred {e}')


# Find/click strategy name
try:
    link = driver.find_element(By.XPATH, '//*[@id="leader"]/div/table/tbody/tr/td[1]/span[2]')
    link.click()

except Exception as e:
    print(f'An error occurred {e}')


time.sleep(5)

# Find/click Enter Trade

try:
    trade_link = driver.find_element(By.XPATH, '//*[@id="strategyMenu"]/li[3]/a/span[1]')
    trade_link.click()

except Exception as e:
    print(f'An error occurred {e}')


time.sleep(60)

# close = input("Press any key to close browser: ")


driver.quit()
print('Driver closed')


