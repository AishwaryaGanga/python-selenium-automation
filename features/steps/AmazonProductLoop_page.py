from selenium.webdriver.common.by import By
from behave import given, when, then

CHECK_PRODUCT_NAME = (By.CSS_SELECTOR,'.a-size-mini.a-spacing-none.a-color-base')
CHECK_PRODUCT_IMAGE = (By.CSS_SELECTOR, '.a-section.aok-relative.s-image-square-aspect')
#CHECK_PRODUCT_IMAGE = (By.CSS_SELECTOR, '.s-image[data-image-latency="s-product-image"]')
WHOLE_BLOCK = (By.CSS_SELECTOR, '.a-section.a-spacing-base')


@given('Open the search result page.')
def open_search_result(context):
    context.driver.get('https://www.amazon.com/s?k=coffee&crid=3MSJWFMI487WB&sprefix=coffee%2Caps%2C140&ref=nb_sb_noss_1')

@then('Verify has a product name.')
def product_name(context):
    name = context.driver.find_elements(*CHECK_PRODUCT_NAME)
    print(len(name))

@then('Verify has a image of the products.')
def product_img(context):
    image = context.driver.find_elements(*CHECK_PRODUCT_IMAGE)
    print(len(image))

@then('Check block has name and image.')
def check_block(context):
    products = context.driver.find_elements(*WHOLE_BLOCK)

    for prod in products:
        title = prod.find_element(*CHECK_PRODUCT_NAME).text
        print('\n\n',title)
        assert title, 'Error!Its blank'
        prod.find_element(*CHECK_PRODUCT_IMAGE)
        print('Img Element:',prod.find_element(*CHECK_PRODUCT_IMAGE))





