import re
from bs4 import BeautifulSoup

def find_model(main_deets):
    """Finds the set's Featured Model"""
    model_left_trim = main_deets.find("Featuring") + 18
    model_trimmed_left = main_deets[model_left_trim:]
    model_left_trim2 = model_trimmed_left.find(">") + 1
    model_trimmed_left2 = model_trimmed_left[model_left_trim2:]
    model_right_trim = model_trimmed_left2.find('<')
    model = model_trimmed_left2[:model_right_trim]
    return model

def find_release(main_deets):
    """Finds the set's Release Date"""
    release_left_trim = main_deets.find("Released") + 17
    release_trimmed_left = main_deets[release_left_trim:]
    release_right_trim = release_trimmed_left.find('<')
    release_date = release_trimmed_left[:release_right_trim]
    return release_date

def find_photog(main_deets):
    """Finds the set's photographer"""
    photog_left_trim = main_deets.find("Photographer:") + 21
    photog_trimmed_left = main_deets[photog_left_trim:]
    photog_left_trim2 = photog_trimmed_left.find(">") + 1
    photog_trimmed_left2 = photog_trimmed_left[photog_left_trim2:]
    photog_right_trim = photog_trimmed_left2.find('<')
    photog = photog_trimmed_left2[:photog_right_trim]
    return photog

def is_video(info_str):
    """Determines if the update is a video"""
    video = str(info_str)
    if video.find('runtime') > 0:
        return True

# opens the file that we've saved and turns it into soup
with open('18.9.15 page.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

loops = 0
print('-' * 140)
for info in soup.findAll('div', class_='pull-left custom-list-item-detailed-photo-stats'):
    if loops < 30:
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
