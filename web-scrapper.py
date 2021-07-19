import requests
from bs4 import BeautifulSoup as bs
import csv

# prompt user for github username, determine url, and pass to BeautifulSoup
github_user = input('Input Github Username: ')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')

# scrap profile image and pinned repositories
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
repositories = soup.find_all('span', {'class': 'repo'})

# open csv file and write header
file = open('github_users.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(file)
writer.writerow([github_user])

# print scraped image url and pinned repositories
print(profile_image)
writer.writerow([profile_image])
for repo in repositories:
    print(repo.text)
    writer.writerow([repo.text])

# close csv file
file.close()