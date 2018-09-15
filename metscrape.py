""" A script that will parse through the data on Met-Art.com"""

from bs4 import BeautifulSoup
import requests

# opens the file that we've saved and turns it into soup
with open('18.9.15 page.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# Loop through 5 sets and display the info to the console
looper = 0
for set_info in soup.findAll('div', class_='custom-list-item-detailed-photo-stats'):
    if looper < 5:
        set_meta = set_info.findAll('span', class_="custom-age")
        if len(set_meta) < 3:
            continue
        else:
            # print(set_info)

            set_name = set_info.h3.text
            set_url = set_info.h3.a['href']
            print(set_name)
            print(set_url)

            for data_point in set_meta:
                print(data_point.text)
            
            print("-" * 100)
        looper += 1
    else:
        break