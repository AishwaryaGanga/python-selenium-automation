from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path='/Users/vaishnavisethuraman/QA/python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get("https://www.amazon.com/")

driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
expected_result = 'Sign-In'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result == actual_result, f'Expected{expected_result} but got {actual_result}'
print('Test case passed')

driver.find_element(By.ID, 'ap_email')

driver.quit()