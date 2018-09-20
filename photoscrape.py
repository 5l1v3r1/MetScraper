from bs4 import BeautifulSoup as bs
from scrape_fun import *
import csv
from datetime import datetime

# opens the file that we've saved and turns it into soup
with open('pages/18.9.19 page.html') as html_file:
    soup = bs(html_file, 'lxml')

returns_path = 'output/test_output.csv'
file = open(returns_path, 'w', newline ='')
writer = csv.writer(file)
writer.writerow(['Release Date', 'Set Name', 'Model(s)', 'Artist', 'Images/Duration', 'Community Rating', "URL"])

print('Scraping data...')

for info in soup.findAll('div', class_='pull-left custom-list-item-detailed-photo-stats')[:]:
    # Using a loop to only grab a certain number of results until I have everything set the
    # I want and then will upate to not loop.
    main_deets = info.findAll('span', class_='custom-age')
    if len(main_deets) < 3:
        continue
    else:
        release_date, set_name, set_model, artist, img_time, set_rated, set_url = get_set_info(info, main_deets)
        writer.writerow([release_date, set_name, set_model, artist, img_time, set_rated, set_url])

        print(f'Date: {release_date} - Set: {set_name} - Saved to: {returns_path}')

file.close()
