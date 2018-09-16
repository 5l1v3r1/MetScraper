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