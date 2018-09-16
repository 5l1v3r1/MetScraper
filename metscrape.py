""" A script that will parse through the data on Met-Art.com"""
""" This is the original file that I created, but didn't like it, so I started from scratch and have something I like better """
""" See photoscrape.py instead """

import re
from bs4 import BeautifulSoup

# opens the file that we've saved and turns it into soup
with open('18.9.15 page.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

regex_duration = re.compile('\d{2}\:\d{2}')
regex_rating = re.compile('\d\.\d{2}')

# Loop through 30 sets and display the info to the console
looper = 0

for set_info in soup.findAll('div', class_='custom-list-item-detailed-photo-stats'):
    if looper < 30:
        set_meta = set_info.findAll('span', class_='custom-age')
        if len(set_meta) < 3:
            continue
        else:
            # variable declaration for set data
            set_name = set_info.h3.text
            set_url = set_info.h3.a['href']
            set_stats = set_info.find('ul', class_='list-unstyled list-inline custom-photo-details')
            photos = set_stats.find('li', class_='custom-photo-details-medias').text

            try:
                num_of_photos = f"Number of photos: {photos}"
                duration = "Duration: 0:00"
            except AttributeError:
                pass

            # Runs Regular Expression tests on data to determine data type and returns the data
            set_stats_clean = str(set_stats).split('\n')


            for test_str in set_stats_clean:
                if regex_duration.findall(test_str):
                    duration = f"Duration: {regex_duration.findall(test_str)[0]}"
                    num_of_photos = "Number of photos: 0"
                else:
                    pass

                if regex_rating.findall(test_str):
                    comm_rating = f"Community Score: {regex_rating.findall(test_str)[0]}"

            # print data to console
            print('-' * 100)
            print(set_name)
            print(set_url)

            for publish_info in set_meta:
                print(publish_info.text)

            print(comm_rating)

            try:
                print(num_of_photos)
            except NameError:
                pass

            try:
                print(duration)
            except NameError:
                pass
        looper += 1
    else:
        break
