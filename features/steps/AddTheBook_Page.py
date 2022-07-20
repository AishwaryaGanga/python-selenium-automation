from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep

CLICK_ADD_TO_CART = (By.CSS_SELECTOR, '#add-to-cart-button')

@when("Add the product to cart")
def add_cart(context):
        context.driver.find_element(*CLICK_ADD_TO_CART).click()
        sleep(2)