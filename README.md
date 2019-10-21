# twitterScraper

A tool to collect the all or some of the tweets from an individual and store them in human readable format, as well as parse them for keywords or phrases. Allows a user to collect tweets beyond the 3200-tweet limit for non twitter developer API users.

##### Warning: this project is currently a little broken, as multithreading is being implemented. It should be up again soon! #####


## Usage: ##

```
python3 main.py [TWITTER URL]
```

## Requirements: ##
* Python 3.7.x
* `BeautifulSoup` 4.1.x+
* Python `requests`

## TODO: ##

* ~Scrape a user's page for tweet objects~
* ~recursively divide user's history based on tweet amount~
* Determine optimal thread amount for scraping






## License
[MIT](https://choosealicense.com/licenses/mit/)
