from selenium.webdriver.common.by import By
from behave import given,when, then

@when ("Click search for {search_book} on product")
def click_search(context, search_book):
        context.driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox').send_keys(search_book)
        context.driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button').click()

@then("Add the product to cart")
def add_cart(context):
        context.driver.find_element(By.CSS_SELECTOR,"div[class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1'] span[class='a-size-medium a-color-base a-text-normal']").click()
        context.driver.find_element(By.CSS_SELECTOR, '#add-to-cart-button').click()


@then("Check the product in cart")
def check_cart(context):
        expected_text = 'Added to Cart'
        actual_text = context.driver.find_element(By.CSS_SELECTOR, '.a-size-medium-plus.a-color-base').text
        assert expected_text == actual_text, f'Expected{expected_text} but got {actual_text}'
        print('Test case passed')
