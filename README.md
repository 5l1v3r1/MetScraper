# MetScraper
Web Scraping data from Met-Art.com

----

**Project primary author**: Eric Greenhalgh
**Project start date**: 9/14/2018

----

The eventual goals of this project are to do the following:
- [X] Scrape individual set data from the site
  - This ended up being something of a challenge since the site requires login access and I ahven't figured out how to work aroudn that.
- [ ] Filter the data and identify relevant data points about each set
  - [X] Currently have the ability to scrape photo data - need to adjust to get video data as well.
  - [ ] Also need to be able to account for multiple-model sets/vids
- [ ] Store the data in a database
  - [X] Export data to CSV
  - [ ] Export data to database
- [ ] Perform useful analysis on the stored data
- [ ] Provide feedback to the site as part of the site's community
- [ ] Track changes in data over the course of time

Dependancies:
Package        | Version
-------------- | -------
beautifulsoup4 | 4.6.3
bs4            | 0.0.1
lxml           | 4.2.5
SQLAlchemy     | 1.2.11