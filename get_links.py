from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
import time

driver =webdriver.Chrome()
url = "https://www.youtube.com/results?search_query=angry+person"
driver.get(url)
for i in range(10):
    time.sleep(1)
    driver.execute_script(f"window.scrollTo(0,10000*{i})")
soup = bs(driver.page_source, 'html.parser')
driver.quit()
res = soup.find_all('a', id = 'thumbnail')
print(res)
count = 0
for thumbnail in res:
    if(thumbnail.get("href")):
       count += 1
print(count)





