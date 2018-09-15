from bs4 import BeautifulSoup
import requests

# opens the file that we've saved and turns it into soup
with open('upcoming.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

content = soup.find('ul', class_='list-inline list-unstyled custom-trending-galleries v-offset-25')
update = content.find('div', class_='custom-trending-information')

model_name = update.a.text
proj_date = update.find('span', class_='custom-trending-date').text
views = update.find('li', class_='custom-activity-stats-views').text

print(proj_date + '\t\t' + model_name + '\t\t' + views)