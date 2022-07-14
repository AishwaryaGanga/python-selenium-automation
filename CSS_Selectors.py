from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path='/Users/vaishnavisethuraman/QA/python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get("https://www.amazon.com/")

driver.find_element(By.CSS_SELECTOR, "[href*='/gp/css/order-history'].nav-a.nav-a-2.nav-progressive-attribute").click()
expected_text = 'Sign-In'
actual_text = driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small').text
assert expected_text == actual_text, f'Expected{expected_text} but got {actual_text}'
print('Test case passed')
assert driver.find_element(By.CSS_SELECTOR, "input[type='email'][maxlength='128']#ap_email[name='email'].a-input-text.a-span12").is_displayed()

driver.quit()