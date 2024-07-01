
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()  # Or any other browser driver
driver.get('https://www.example.com')


#   Interacting with Web Elements
button = driver.find_element(By.ID, 'submit-button')
button.click()


#   Typing into a Text Field
text_field = driver.find_element(By.NAME, 'username')
text_field.send_keys('my_username')


#   Selecting from a Dropdown Menu
dropdown = Select(driver.find_element(By.NAME, 'options'))
dropdown.select_by_visible_text('Option 1')


# 3. Extracting Information
element = driver.find_element(By.CLASS_NAME, 'headline')
print(element.text)


# Getting Attributes of an Element
image = driver.find_element(By.TAG_NAME, 'img')
src = image.get_attribute('src')
print(src)


#   Handling Alerts and Pop-ups
alert = driver.switch_to.alert
alert.accept()


# Handling Frames and Windows
driver.switch_to.frame('frame_name')


#   Switching to a Window
driver.switch_to.window(driver.window_handles[1])


#   Scrolling the Page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# Taking Screenshots


driver.save_screenshot('screenshot.png')


#   Executing JavaScript
driver.execute_script("alert('Hello, world!');")


#   Working with Cookies
cookie = {'name': 'foo', 'value': 'bar'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(cookies)
#   Waiting for Elements


element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'myElement'))
)

