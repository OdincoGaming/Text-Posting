import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from time import sleep
import re


#//*[@id="u_0_2"]
#//*[@id="js_tm"]
def MakePost():
    statusMessage = input('input message to post \n')
    statuselement = driver.find_element(By.XPATH,'.//*[@name="xhpc_message"]')
    time.sleep(3)
    statuselement.send_keys(statusMessage)
    time.sleep(3)
    buttons = driver.find_element_by_tag_name('button')
    for button in buttons:
        if button.text == 'Post':
            button.click()
    time.sleep(3)

def Login(e, p):
    try:
        emailelement = driver.find_element(By.XPATH,'.//*[@id="email"]')
    except:
        emailelement = driver.find_element(By.XPATH,'.//*[@name="email"]')
    try:
        passelement = driver.find_element(By.XPATH,'.//*[@id="pass"]')
    except:
        passelement = driver.find_element(By.XPATH,'.//*[@name="pass"]')
    try:
        loginButton = driver.find_element(By.XPATH,'.//*[@id="loginbutton"]')
    except:
        loginButton = driver.find_element(By.XPATH,'.//*[@name="loginbutton"]')
    emailelement.send_keys(e)
    passelement.send_keys(p)
    loginButton.click()
    time.sleep(3)

def AnalyzeFeed():
    postIds = driver.find_elements_by_class_name('_81hb')
    i = 0
    postReacts = postIds
    while i < (len(postIds)):
        postReacts[i] = postIds[i].text
        postReacts[i] = ''.join(re.findall(r'\d+',postReacts[i]))
        print(postReacts[i])
        i += 1


_browser_profile = webdriver.FirefoxProfile()
_browser_profile.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(firefox_profile=_browser_profile)
driver.get('http://facebook.com')
email = input('input email \n')
password = input('input password \n')
Login(email, password)
AnalyzeFeed()


