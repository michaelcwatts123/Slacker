from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule
import argparse

def signOn(driver):
    fName = driver.find_element_by_id('email')
    fName.send_keys(args.username)

    lName = driver.find_element_by_id('password')
    lName.send_keys(args.password)
    lName.send_keys(Keys.ENTER)
    
def ping():
    driver = webdriver.Chrome('tools/chromedriver')
    driver.get('https://'+args.domain+'.slack.com/')
    signOn(driver)
    driver.find_elements_by_class_name('p-channel_sidebar__you_label')[0].click()
    txtBox2 = driver.find_element_by_tag_name('p')
    txtBox2.send_keys('ping')
    txtBox2.send_keys(Keys.ENTER)
    driver.quit()
    
def job():
    for i in range(16):
        ping()
        time.sleep(1740)
    
parser = argparse.ArgumentParser()
parser.add_argument('--domain')
parser.add_argument('--username')
parser.add_argument('--password')
args = parser.parse_args()

schedule.every().monday.at("09:00").do(job)
schedule.every().tuesday.at("09:00").do(job)
schedule.every().wednesday.at("09:00").do(job)
schedule.every().thursday.at("09:00").do(job)
schedule.every().friday.at("09:00").do(job)



while True:
    schedule.run_pending()
    time.sleep(1)
