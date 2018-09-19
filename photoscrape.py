from bs4 import BeautifulSoup as bs
from scrape_fun import *
import csv, re
from datetime import datetime

# opens the file that we've saved and turns it into soup
with open('pages/Michelle_h_sets.html') as html_file:
    soup = bs(html_file, 'lxml')

returns_path = 'output/test_output.csv'
file = open(returns_path, 'w', newline ='')
writer = csv.writer(file)
writer.writerow(['Release Date', 'Set Name', 'Models', 'Photographer', '# of Photos', 'Community Rating', "URL"])

for info in soup.findAll('div', class_='pull-left custom-list-item-detailed-photo-stats')[:]:
    # Using a loop to only grab a certain number of results until I have everything set the
    # I want and then will upate to not loop.
    if is_video(info):
        continue
    else:
        # regex declarations
        reg_date = re.compile(r'\w{3}\s\d{1,2},\s\d{4}')
        reg_featuring = re.compile(r'Featuring:\s(.*)')
        reg_photoDir = re.compile(r'(Director|Photographer):\s(.*)')

        # Turn the details into a list
        main_deets = info.findAll('span', class_='custom-age')
        print(main_deets)
        # Find the data and store them in variables
        set_name = info.h3.text
        set_url = info.h3.a['href']
        release_date = reg_date.search(main_deets[0].text).group()
        set_model = reg_featuring.search(main_deets[1].text).group(1).replace(',', ' -')
        photographer = reg_photoDir.search(main_deets[2].text).group(2)
        set_rated = info.find('li', class_='custom-activity-stats-rating').text
        photo_num = info.find('li', class_='custom-photo-details-medias').text

        writer.writerow([release_date, set_name, set_model, photographer, photo_num, set_rated, set_url])

        """ print(f'Published: {release_date:<20} Set Name: {set_name:<25} Featuring: {set_model}')
        print(f'Photos By: {photographer:<20} # of Photos: {photo_num:<22} Rated: {set_rated}')
        print(set_url)
        #print(info)
        print('-' * 140) """

file.close()
