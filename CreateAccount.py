from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path='/Users/vaishnavisethuraman/QA/python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&mobileBrowserWeblabTreatment=T1&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&prevRID=QV8W248Q88K5578FCXC5&openid.assoc_handle=usflex&openid.mode=checkid_setup&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
#by CSS class(es)
driver.find_element(By.CSS_SELECTOR,'i.a-icon.a-icon-logo')


#by CSS class
driver.find_element(By.CSS_SELECTOR,'h1.a-spacing-small')

#by CSS id
driver.find_element(By.CSS_SELECTOR,'#ap_customer_name')
driver.find_element(By.CSS_SELECTOR,'input#ap_email')
driver.find_element(By.CSS_SELECTOR,'#continue')

#by CSS type attribute
driver.find_element(By.CSS_SELECTOR,"input[type='password'][id='ap_password']")#multiple attributes
driver.find_element(By.CSS_SELECTOR,"input[name='passwordCheck']")

#by CSS Href attribute
driver.find_elemen(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#by Paritial match
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use?']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice?']")
driver.find_element(By.CSS_SELECTOR, "[href*='/ap/signin?openid.pape.max_auth']")