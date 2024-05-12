# Extracts movie ids to file (ids.txt)


import re
from config import *


pattern: str = f'"__ref":"Film:(\d+)"'

with open(PAGES_FILE, 'r') as f:
  matches = re.findall(pattern, f.read())
  with open(IDS_FILE, 'w') as f:
    f.write('\n'.join(matches))