from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click on the cart icon')
def open_amazon(context):
    context.driver.find_element(By.CSS_SELECTOR, '.nav-cart-icon.nav-sprite').click()

@then('Verify your amazon cart is empty')
def open_amazon(context):
    expected_text = 'Your Amazon Cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_text == actual_text, f'Expected{expected_text} but got {actual_text}'

