#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import sys

if len(sys.argv) < 3 or len(sys.argv) > 3:
    print("Usage: python WebScraper.py <URL> <Keyword> ")
    exit()
url = sys.argv[1]
search_string = sys.argv[2]
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

python_jobs = soup.find_all('h2',
                            string=lambda text: search_string in text.lower())

print(f"Match Results:{len(python_jobs)}")

for p in python_jobs:
    link = p.find('a')['href']
    print(p.text.strip())
    print(f"Apply here:{link}\n")