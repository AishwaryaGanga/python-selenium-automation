from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep

PRODUCT_BOOK = (By.CSS_SELECTOR, '.a-size-medium.a-color-base.a-text-normal')

@when('Click on the book')
def click_book(context):
        context.driver.find_element(*PRODUCT_BOOK).click()
        sleep(2)