from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path='/Users/vaishnavisethuraman/QA/python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get("https://www.amazon.com/")

driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
expected_text = 'Sign-In'
actual_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_text == actual_text, f'Expected{expected_text} but got {actual_text}'
print('Test case passed')

assert driver.find_element(By.ID, 'ap_email').is_displayed()

driver.quit()