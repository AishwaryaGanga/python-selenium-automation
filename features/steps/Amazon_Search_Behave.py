from selenium.webdriver.common.by import By
from behave import given,when, then

@given("Open Amazon Page")
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when("Search for word coffee on amazon")
def open_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Coffee')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@then ("Results for coffee shown")
def open_amazon(context):
    expected_result = '"Coffee"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected{expected_result} but got {actual_result}'
    print('Test case passed')