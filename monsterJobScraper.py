#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup

url = "https://www.monster.com/jobs/search/?"
q = input("What job are you looking for? ")
where = input("Where do you plan on working? ")
if q and where:
    url = url + f"q={q}" + f"&where={where}"
else:
    print("Please try again...")
    exit()
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
new_string = ''.join([str(elem) for elem in q])
python_jobs = results.find_all('h2',
                               string=lambda text: new_string in text.lower())

print(f"Match Results:{len(python_jobs)}")

for p in python_jobs:
    link = p.find('a')['href']
    print(p.text.strip())
    print(f"Apply here:{link}\n")