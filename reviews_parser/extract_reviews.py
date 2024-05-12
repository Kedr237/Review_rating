# Extract movie reviews to file (reviews.txt)


import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from typing import List
from typing import Dict
from config import *


reviews_dict: List[Dict[str, str]] = []

with open(IDS_FILE, 'r') as f: # extract ids as list
  ids: List[int] = f.read().split('\n')

driver = webdriver.Chrome()
driver.get(TOP_500)
time.sleep(6)

for id in ids:
  print(id)
  reviews_dict = []
  driver.get(get_reviews_page(id))
  time.sleep(1)
  review_elements = driver.find_elements(By.CLASS_NAME, 'response')

  for element in review_elements:
    try:
      review_body = element.find_elements(By.CLASS_NAME, 'brand_words')
      review_body_text = review_body[0].text
      classes = element.get_attribute('class')
      class_list = classes.split()
      reviews_dict.append({class_list[-1]: review_body_text})
    except:
      pass

  with open(REVIEW_FILES + str(id) + '.json', 'w', encoding='utf-8') as f:
    json.dump(reviews_dict, f, ensure_ascii=False)
