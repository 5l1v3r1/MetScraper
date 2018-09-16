import re
from bs4 import BeautifulSoup
from scrape_fun import *

# opens the file that we've saved and turns it into soup
with open('18.9.16 page.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

loops = 0
print('-' * 140)
for info in soup.findAll('div', class_='pull-left custom-list-item-detailed-photo-stats'):
    # Using a loop to only grab a certain number of results until I have everything set the
    # I want and then will upate to not loop.
    if loops < 20:
        if is_video(info):
            continue
        else:
            main_deets = str(info.findAll('span', class_='custom-age'))

            set_name = info.h3.text
            release_date = find_release(main_deets)
            set_model = find_model(main_deets)
            set_rated = info.find('li', class_='custom-activity-stats-rating').text
            photo_num = info.find('li', class_='custom-photo-details-medias').text
            photographer = find_photog(main_deets)

            print(f'Published: {release_date:<20} Set Name: {set_name:<25} Featuring: {set_model}')
            print(f'Photos By: {photographer:<20} # of Photos: {photo_num:<22} Rated: {set_rated}')
            #print(info)
            print('-' * 140)
            loops += 1
    else:
        break
