import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json

with urlopen('https://jsonmock.hackerrank.com/api/movies/search/?Title=spiderman') as response:
    html = response.read()
    parsed = json.loads(html.decode('utf-8'))
    pages = parsed['total_pages']


titles = []
for page in range(1,pages+1):
    with urlopen('https://jsonmock.hackerrank.com/api/movies/search/?Title=spiderman&page={}'.format(page)) as response:
        html = response.read()
        parsed = json.loads(html.decode('utf-8'))

    for Poster in parsed['data']:
        titles.append(Poster['Title'])

titles.sort()
[print(i) for i in titles]




