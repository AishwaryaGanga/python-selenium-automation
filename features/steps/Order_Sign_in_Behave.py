from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon.com page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")

@when('Click order and Return tab')
def open_amazon(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()

@then('Open amazon sign in page')
def open_amazon(context):
    expected_text = 'Sign-In'
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_text == actual_text, f'Expected{expected_text} but got {actual_text}'

@then('check email_Id space')
def open_amazon(context):
    assert context.driver.find_element(By.ID, 'ap_email').is_displayed()