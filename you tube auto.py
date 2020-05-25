'''1.import selenium package
   2.download chrome driver
   3.place the doc of chrome driver and code in same folder
   
'''
from selenium import webdriver
'''webdriver pkg is a WebDriver is a web
automation framework that allows you to execute your tests against different browsers,
not just Firefox, Chrome (unlike Selenium IDE).
WebDriver also enables you to use a programming language in creating your
test scripts (not possible in Selenium IDE)'''
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.youtube.com")
##assert "you tube" in driver.title
search=driver.find_element_by_name('search_query')
search.send_keys('buttabomma song')  
searchbutton=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbutton.click()
select=driver.find_element_by_xpath('//*[@id="dismissable"]')#first serach mov is played
select.click()
##search.send_keys(Keys.RETURN)#Keys.RETURN K is captital
##assert "No result found." not in driver.page_source
##

##from selenium import webdriver
##
##browser = webdriver.Chrome()
##browser.get('http://seleniumhq.org/')

