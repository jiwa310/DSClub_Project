import time, datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Change before use
browser = webdriver.Chrome('/Users/hongtan/Downloads/chromedriver')

search = "angry joe"

#browser.get(f'https://www.youtube.com/results?search_query={search}')

browser.get('https://en.y2mate.is/95/')

time.sleep(2)

link = browser.find_element_by_id('txtUrl')
link.send_keys('https://www.youtube.com/watch?v=qZ90POH8JlA')

start = browser.find_element_by_xpath('/html/body/section[1]/div/div[2]/div[1]/div/form/button/span[1]')
start.click()

time.sleep(2)

btn = browser.find_element_by_xpath('/html/body/section[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/button')
btn.click()

time.sleep(1)

downloadbtn = browser.find_element_by_xpath('/html/body/section[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/button/a')
downloadbtn.click()

# link.click()