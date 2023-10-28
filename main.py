import requests
from bs4 import BeautifulSoup

# Web Scrap

# constants
total_pages = 5
entries_per_page = 50

# list to store data
info_anime_titles = []

# for loop
for i in range(total_pages):

    listings = entries_per_page * i

    # url
    url = f'https://myanimelist.net/topanime.php?limit={listings}'

    # GET requests
    r = requests.get(url)

    # parcing the html
    soup = BeautifulSoup(r.content, 'html.parser')

    # print out wanted information
    s = soup.find('div', class_='wrapper')
    content = s.find_all('h3')

    for t in content:
        info_anime_titles.append(t.text)

# print data
for title in info_anime_titles:
    print(title)