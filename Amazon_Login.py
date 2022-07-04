from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path='/Users/vaishnavisethuraman/QA/python-selenium-automation/chromedriver')
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

driver.find_element(By.XPATH, "//a[@href='/ref=ap_frn_logo']") # By Attribute
driver.find_element(By.XPATH, "//input[@id='ap_email']")

#By multiple attributes
driver.find_element(By.XPATH,"//input[@type='submit' and @aria-labelledby='continue-announce']")

driver.find_element(By.XPATH, "//span[contains(text(), 'Need help?')]") # By text
driver.find_element(By.XPATH, "//a[@id = 'createAccountSubmit']")