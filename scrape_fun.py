import re

def is_video(info_str):
    """Determines if the update is a video"""
    video = str(info_str)
    if video.find('runtime') > 0:
        return True

def get_set_info(info, main_deets):
    # regex declarations
    reg_date = re.compile(r'\w{3}\s\d{1,2},\s\d{4}')
    reg_featuring = re.compile(r'Featuring:\s(.*)')
    reg_photoDir = re.compile(r'(Director|Photographer):\s(.*)')
    # Turn the details into a list
    sub_deets = info.find('ul', class_='list-unstyled list-inline custom-photo-details')
    det_split = sub_deets.findAll('li')
    # print(main_deets)
    # Find the data and store them in variables
    set_name = info.h3.text
    set_url = info.h3.a['href']
    release_date = reg_date.search(main_deets[0].text).group()
    set_model = reg_featuring.search(main_deets[1].text).group(1).replace(',', ' -')
    artist = reg_photoDir.search(main_deets[2].text).group(2)
    img_time = det_split[0].text
    set_rated = det_split[1].text
    return release_date, set_name, set_model, artist, img_time, set_rated, set_url