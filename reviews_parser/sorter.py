import os
import json
from typing import List
from typing import Dict
from typing import Final
from config import *


def get_folder_contents(folder) -> List[str]:
  return [os.path.join(folder, file) for file in os.listdir(folder)]

GENERATED: Final[str] = 'reviews_parser/' + FILES_DIRECTORY
review_files: List[str] = get_folder_contents(GENERATED + 'all_reviews/')
good_reviews: List[str] = []
bad_reviews: List[str] = []
neural_reviews: List[str] = []
review_scores: Dict[str, List[str]] = {
  'good': good_reviews,
  'bad': bad_reviews,
  'neutral': neural_reviews
}
max_reviews: int = 2000

for reviews_file in review_files:
  reviews_by_category: Dict[str, int] = {
    'good': 10,
    'bad': 10,
    'neutral': 10
  }
  with open(reviews_file, 'r') as f:
    reviews = json.load(f)
    for review in reviews:
      for score, text in review.items():
        if len(review_scores[score]) < max_reviews and reviews_by_category[score] > 0:
          review_scores[score].append(text)
          reviews_by_category[score] -= 1
 
with open(GENERATED + f'sorted_by_{max_reviews}.json', 'w', encoding='utf-8') as f:
  json.dump(review_scores, f, ensure_ascii=False)