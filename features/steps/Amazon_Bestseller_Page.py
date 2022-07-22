from selenium.webdriver.common.by import By
from behave import given,when, then

BEST_SELLER = (By.CSS_SELECTOR,'._p13n-zg-nav-tab-all_style_zg-tabs-li-selected-div__3tHnP')
LIST_ITEMS=(By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR")

@given('Open Amazon Bestseller page')
def best_seller_page(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")

@then('Check BestSeller Tabs on the page')
def check_links(context):
    print(context.driver.find_element(*BEST_SELLER))

@then('Verify the {expected_tabs}')
def verify_page(context,expected_tabs):
    expected_tabs = int(expected_tabs)
    results = context.driver.find_elements(*LIST_ITEMS)
    assert len(results)==expected_tabs,f'Expected {expected_tabs} links but got {len(results)}'