from selenium.webdriver.common.by import By
from behave import given, when, then

CHECK_PRODUCT_NAME = (By.CSS_SELECTOR,'.a-size-mini.a-spacing-none.a-color-base')
CHECK_PRODUCT_IMAGE = (By.CSS_SELECTOR, '.a-section.aok-relative.s-image-square-aspect')
WHOLE_BLOCK = (By.CSS_SELECTOR, '.a-section.a-spacing-base')


@given('Open the search result page.')
def open_search_result(context):
    context.driver.get('https://www.amazon.com/s?k=coffee&crid=3MSJWFMI487WB&sprefix=coffee%2Caps%2C140&ref=nb_sb_noss_1')

@then('Verify has a {expected_name}.')
def product_name(context,expected_name):
    actual_name = context.driver.find_elements(*CHECK_PRODUCT_NAME).text
    assert expected_name == actual_name, f'expected{expected_name} but got {actual_name}'

@then('Verify has a {expected_img}.')
def product_img(context, expected_img):
    actual_img = context.driver.find_elements(*CHECK_PRODUCT_IMAGE)
    assert expected_img == actual_img, f'expected{expected_img} but got {actual_img}'

@then('Check block has {expected_result}')
def check_block(context, expected_result):
    for prod in check_block:
        product = context.driver.find_elements(*WHOLE_BLOCK)
        title = prod.find_elemet(*CHECK_PRODUCT_NAME).text
        img = prod.find_elemet(*CHECK_PRODUCT_IMAGE)





