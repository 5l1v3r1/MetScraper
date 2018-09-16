import re
from bs4 import BeautifulSoup

def find_model(main_deets):
    """Finds the set's Featured Model"""
    model_left_trim = main_deets.find("Featuring") + 18
    model_trimmed_left = main_deets[model_left_trim:]
    model_right_trim = model_trimmed_left.find('<')
    model = model_trimmed_left[:model_right_trim]
    return model

def find_rating(info_str):
    rating_left_trim = info_str.find('rating') + 8
    rating_trimmed_left = info_str[rating_left_trim:]
    rating_right_trim = rating_trimmed_left.find('<')
    rating = rating_trimmed_left[:rating_right_trim]
    return rating

def find_release(main_deets):
    """Finds the set's Release Date"""
    release_left_trim = main_deets.find("Released") + 17
    release_trimmed_left = main_deets[release_left_trim:]
    release_right_trim = release_trimmed_left.find('<')
    release_date = release_trimmed_left[:release_right_trim]
    return release_date

def is_video(info_str):
    """Determines if the update is a video"""
    video = str(info_str)
    if video.find('runtime'):
        return True

# opens the file that we've saved and turns it into soup
with open('18.9.15 page.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

info = soup.find('div', class_='pull-left custom-list-item-detailed-photo-stats')
main_deets = str(info.findAll('span', class_='custom-age'))

set_name = info.h3.text
release_date = find_release(main_deets)
set_model = find_model(main_deets)
set_video = is_video(info)
set_rated = find_rating(str(info))

print(f'Set Name: {set_name} Published: {release_date} Featuring: {set_model} Rated: {set_rated}')
