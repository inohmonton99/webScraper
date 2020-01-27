#!/usr/bin/env python
# coding: utf-8

import json
import csv
from bs4 import BeautifulSoup as bs
import os
import requests

url = "https://www.ebay.com/sch/i.html?_nkw="
keyword = input("What are you searching for? ")
if not keyword:
    print("Please try again...")
    exit()

new_url = url + keyword
page = requests.get(new_url)
soup = bs(page.content, "html.parser")
results = soup.find(id="mainContent")
containers = results.find_all("div", class_="s-item__wrapper clearfix")

print("Matches found: {}".format(len(containers)))

filename = "ebay.csv"
f = open(filename, "wt")
headers = 'brand, price, shipping, item_hotness, returns \n'
f.write(headers)

for i in containers:
    brand = i.div.div.a.img["alt"]
    brand = brand.strip()
    price = i.find_all("span", class_="s-item__price")
    price = price[0].text.strip()
    try:
        shipping = i.find_all("span", class_="s-item__shipping s-item__logisticsCost")
        shipping = shipping[0].text.strip()
        item_hotness = i.find_all("span", class_="s-item__hotness")
        item_hotness = item_hotness[0].text.strip()
        returns = i.find_all("span", class_="s-item__free-returns s-item__freeReturnsNoFee")
        returns = returns[0].text.strip()
    except IndexError as exc:
        shipping = str(shipping).replace("[]", "")
        item_hotness = str(item_hotness).replace("[]", "")
        returns = str(returns).replace("[]", "")
    f.write(brand.replace(",", "") + ',' + price.replace(",", "") + ',' + shipping.replace(",", "") + ','
            + item_hotness.replace(",", "") + ',' + returns.replace(",", "") + "\n")

print("File saved to {}".format(os.path.relpath(filename)))
