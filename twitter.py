from bs4 import BeautifulSoup
import requests
import re
from datetime import *

def pullTwitter(username, period_start = None, period_end = None, filter = []):
    pass
    # timeline = page.select('#timeline li.stream-item')
    # for tweet in timeline:
    #     tweet_id = tweet['data-item-id']
    #     tweet_text = tweet.select('p.tweet-text')[0].get_text()
    #     tweet_library.append({"id": tweet_id, "text": tweet_text})
    # return(tweet_library)

def recursiveTwitter(username, start, end, list = []):
    page = None
    tweet_library = []
    #try:
    if start == None:
        page = BeautifulSoup(requests.get('https://twitter.com/' + username).text, 'html.parser')
    else:
        print(start.isoformat())
        print(end.isoformat())
        page_url = 'https://twitter.com/search?l=&q=from%3A' + username +\
         '%20since%3A' + start.isoformat() + 'until%3A' + end.isoformat() + '&src=typd&lang=en'
        print(page_url)
        page = BeautifulSoup(requests.get(page_url).text, 'html.parser')

    #except: print("couldn't reach " + username + "'s account. Please check your connection")
    #timePartitionListWrapper(getStartDate(username), username)
    timeline = page.find_all("div", class_ = "stream")
    print(timeline)
    #print(len(timeline))
    for tweet in timeline:
        tweet_id = tweet['data-item-id']
        print(tweet_id)
        tweet_text = tweet.select('p.tweet-text')[0].get_text()
        tweet_library.append({"id": tweet_id, "text": tweet_text})
    print(len(tweet_library))
    if(len(tweet_library) > 19): #needs timedelta
        return recursiveTwitter(username, start, end)
    return tweet_library

def getStartDate(username):
    try:
        page = BeautifulSoup(requests.get('https://twitter.com/' + username).text, 'html.parser')
    except: print("couldn't reach " + username + "'s account. Please check your connection")
    date = page.find('span',{'class':'ProfileHeaderCard-joinDateText js-tooltip u-dir'}).get_text()
    month = date.split()[1]
    year = date.split()[2]
    return(datetime(int(year), month_string_to_number(month), 1))

def timePartitionListWrapper(username, start_date = datetime.utcfromtimestamp(0)):
    if start_date == datetime.utcfromtimestamp(0):
        start_date = getStartDate(username)

    curr_date = datetime.now()
    while(start_date < curr_date):
        recursiveTwitter(username, start_date, start_date + timedelta(days=7))
        start_date = start_date + timedelta(days=7)

#from stackexchange user: harryh
def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
        'may':5,
        'jun':6,
        'jul':7,
        'aug':8,
        'sep':9,
        'oct':10,
        'nov':11,
        'dec':12
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')
