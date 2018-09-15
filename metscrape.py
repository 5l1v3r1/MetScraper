""" A script that will parse through the data on Met-Art.com"""

from bs4 import BeautifulSoup
import requests

# opens the file that we've saved and turns it into soup
with open('18.9.14 page.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# finds the first set and displys info in the console
set_info = soup.find('div', class_='custom-list-item-detailed-photo-stats')
print(set_info)

set_name = set_info.h3.text
set_url = set_info.h3.a['href']
print(set_name)
print(set_url)

set_meta = set_info.findAll('span', class_="custom-age")
print(len(set_meta))
for data_point in set_meta:
    print(data_point.text)