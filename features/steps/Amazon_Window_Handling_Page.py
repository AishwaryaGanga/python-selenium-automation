from selenium.webdriver.common.by import By
from behave import given, when, then
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PRIVACY_LINK = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")

@given('Open Amazon T&C page')
#@given('Store original windows')
def main_page(context):
    original_window = context.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=508088&ref_=footer_cou')
    print('Originial Window: ', original_window)
    #to scroll down to the element
    context.driver.execute_script("arguments[0].scrollIntoView();", context.driver.find_element(*PRIVACY_LINK))
    sleep(2)

@when('Click on Amazon Privacy Notice link')
def click_privacy(context):
    #context.driver.wait.until(EC.element_to_be_clickable
    # (PRIVACY_LINK),message = 'Not Found').click()
    context.driver.find_element(*PRIVACY_LINK).click()

@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    print('Current Window:', context.driver.window_handles)
    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)

@then('Verify Amazon Privacy Notice page is opened')
def verify_page_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/'))
    sleep(2)

@then('User can close new window and switch back to original')
def close_switch_back(context):
    context.driver.close()
    #context.driver.switch_to.window(old_window)
