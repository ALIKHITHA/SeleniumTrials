from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get('https://en-gb.facebook.com/login')
eml=driver.find_element_by_name('email')
eml.send_keys('jathinadhikamsetty@gmail.com')
pwd=driver.find_element_by_name('pass')
pwd.send_keys('jinnu2646')
login=driver.find_element_by_name('login')
login.click()

