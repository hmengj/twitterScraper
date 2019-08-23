from twitter import pullTwitter, getStartDate, timePartitionListWrapper
from bs4 import BeautifulSoup
import requests
import re
from datetime import *


#getStartDate('umbernhard')
#pullTwitter('umbernhard')
timePartitionListWrapper('umbernhard', datetime.now() - timedelta(weeks = 30))
