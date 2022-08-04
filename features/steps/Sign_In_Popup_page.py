from selenium.webdriver.common.by import By
from behave import given, when, then
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Sign_in_popup = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')

@when('Click on the Sign_in pop up')
def click_pop_up(context):
    context.driver.wait.until(EC.element_to_be_clickable(Sign_in_popup), message="Sign_in not clickable").click()


