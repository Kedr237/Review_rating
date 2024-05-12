# Generates a file (pages.txt) containing movie pages


import time
from selenium import webdriver
from config import *


driver = webdriver.Chrome()

with open(PAGES_FILE, 'w') as f: # clear file
  pass

for page in range(1, COUNT_PAGES+1):
  driver.get(TOP_500 + f'?page={page}')
  time.sleep(2)
  with open(PAGES_FILE, 'a') as f:
    f.write(driver.page_source)

driver.quit()