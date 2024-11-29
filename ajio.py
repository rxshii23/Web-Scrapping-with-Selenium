from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
driver_path = Service("/Users/rushikeshdeshmukh/Downloads/chromedriver-mac-arm64/chromedriver")
chrome_options = Options()

chrome_options.add_experimental_option('detach', True)
chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])

chrome_options.add_argument(('--ignore-certificate-errors'))
chrome_options.add_argument(('--ignore-ssl-errors'))

chrome_options.add_argument(('start-maximized'))
chrome_driver = webdriver.Chrome(service=driver_path, options=chrome_options)

chrome_driver.get('https://www.ajio.com/men-backpacks/c/830201001')

# scrolling webpage

old_height = chrome_driver.execute_script('return document.body.scrollHeight')
print(old_height)

counter = 1
while True:

    chrome_driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = chrome_driver.execute_script('return document.body.scrollHeight')
    print(counter)
    counter += 1
    print(old_height)
    print(new_height)

    if new_height == old_height:
        break

    old_height = new_height

html = chrome_driver.page_source

with open('ajio.html', 'w', encoding='utf-8') as f:
    f.write(html)
