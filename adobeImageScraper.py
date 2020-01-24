#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup as bs
import sys
import shutil
import os

url = "https://stock.adobe.com/ph/search?k="
path = r"D:\Users\Inoh\Desktop\images"
if path:
    os.makedirs(path, exist_ok=True)
    os.chdir(path)

keyword = input("enter search keyword: ")
if not keyword:
    print("keyword is empty!")
    exit()

new_url = url + keyword
page = requests.get(new_url)
soup = bs(page.content, 'html.parser')
results = soup.find_all('a', class_="js-search-result-thumbnail non-js-link")

try:
    for i in results:
        link = i.find('img')['src']
        filename = link[37:]
        r = requests.get(link, stream=True)
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                print("downloading {}".format(filename))
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
except FileNotFoundError as exc:
    print("Files downloaded in {}".format(path))