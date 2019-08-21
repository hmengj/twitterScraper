from bs4 import BeautifulSoup
import requests
import re
import datetime
def pullTwitter(username, period_start = None, period_end = None, filter = []):
    tweet_library = []
    try:
        if period_start == None:
            page = BeautifulSoup(requests.get('https://twitter.com/' + username).text, 'html.parser')
        else:
            page = BeautifulSoup(requests.get('https://twitter.com/search?l=&q=from%3A' + username +\
             '%20since%3A' + period_start + 'until%3A' + period_end + '&src=typd&lang=en').text, 'html.parser')
    except: print("couldn't reach " + username + "'s account. Please check your connection")
    timeline = page.select('#timeline li.stream-item')
    for tweet in timeline:
        tweet_id = tweet['data-item-id']
        tweet_text = tweet.select('p.tweet-text')[0].get_text()
        tweet_library.append({"id": tweet_id, "text": tweet_text})
    return(tweet_library)

def recursiveTwitter(username, start, end, list = []):
    if(list == []):
        list = pullTwitter(username, start, end)
    if(len(list) > 19): #needs timedelta
        recursiveTwitter(username, start, end)
    return list

def getStartDate(username):
    try:
        page = BeautifulSoup(requests.get('https://twitter.com/' + username).text, 'html.parser')
    except: print("couldn't reach " + username + "'s account. Please check your connection")
    date = page.find('span',{'class':'ProfileHeaderCard-joinDateText js-tooltip u-dir'}).get_text()
    month = date.split()[1]
    year = date.split()[2]
    return(datetime.datetime(int(year), month_string_to_number(month), 1))

def timePartitionListWrapper(start_date, username):
    curr_date = datetime.now().date()
    while(start_date < curr_date):
        recursiveTwitter(username, start_date, start_date + datetime.timedelta(days=7))
        start_date = start_date + datetime.timedelta(days=7)




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
