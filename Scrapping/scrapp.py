import requests
from bs4 import BeautifulSoup

data = requests.get("https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm")
# data = requests.get("https://www.linkedin.com/search/results/all/?keywords=afiniti&origin=GLOBAL_SEARCH_HEADER")
soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.prettify())
movieTable = soup.find('table', {'class': 'findList'})
print(movieTable.prettify())
rows = movieTable.findAll('tr')

li = []
for row in rows:
    row_data = row.findAll('td')
    # print(row_data[1].a.text)
    subUrl = row_data[1].a['href']
    subData = requests.get("https://www.imdb.com"+subUrl)
    childSoup = BeautifulSoup(subData.content, 'html.parser')
    if childSoup.find('div', {'class': 'see-more inline canwrap'}):
        genre = childSoup.find('div', {'class': 'see-more inline canwrap'})
        if genre.a.text == " Documentary":
            print(row_data[1].a.text)
            print(genre.a.text)
            li.append(row_data[1].a.text)

print(li)