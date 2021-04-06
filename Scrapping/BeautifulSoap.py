import time

import requests
from bs4 import BeautifulSoup

Url = requests.get('https://www.fastly.com/network-map')
# url1 = requests.get('http://revamp.landbw.co/admin/threads')
soup = BeautifulSoup(Url.content, 'html.parser')
# print(soup.prettify())
# table = soup.find('table', {'class': 'table table-striped table-hover'})
# # print(table.prettify())
time.sleep(2)
RPS = soup.find('div', {'class': 'tachometer-label'})
print(RPS.text)

Hit_Ratio = soup.find('div', {'class': 'tach-stat hit-ratio flex-col'})
print(Hit_Ratio.text)

Hit_time = soup.find('div', {'class': 'tach-stat ttfb flex-col'})
print(Hit_time.text)

Bandwidth = soup.find('div', {'class': 'tach-value'})
print(Bandwidth.text)
