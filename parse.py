__author__ = 'stefan'
import urllib2
import re
import json
from BeautifulSoup import BeautifulSoup
import re

soup = BeautifulSoup(urllib2.urlopen('http://www.6pm.com/mens-shoes~s?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/#!/men-sneakers-athletic-shoes~1').read())
body = soup('div', {'id': 'searchResults'})
paginator = soup('div', {'class': 'pagination'})

for page in paginator[0].findAll('a'):
    print [k for k in page.attrs]
    if re.compile(r"arrow") in [k for k in page.attrs]:
        print page.attrs['class']
items = []
for line in body:
    for row in line.findAll('a'):
        item = dict()
        item['href'] = row['href']
        item['image'] = row.find("img")['src']
        item['data-product-id'] = row['data-product-id']
        item['product-url'] = 'http://www.6pm.com/' + row['data-product-id']
        item['brandName'] = row.find("span", {"class": "brandName"}).string
        item['productName'] = row.find("span", {"class": "productName"}).string
        item['price-6pm'] = float(row.find("span", {"class": "price-6pm"}).string.replace("$", ""))
        item['brand'] = row.find("span", {"class": "brandName"}).string
        items.append(item)
