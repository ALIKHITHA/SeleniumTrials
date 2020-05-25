from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https:\\www.amazon.in")
x=driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[2]')#login step strts
x.click()

eml=driver.find_element_by_id('ap_email').send_keys("7680872646")

continuebutton=driver.find_element_by_id('continue').click()

pwd=driver.find_element_by_id("ap_password").send_keys("likhiamazon")

loginbutton=driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()

search=driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys('coconut oil')  
searchbutton=driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
searchbutton.click()
