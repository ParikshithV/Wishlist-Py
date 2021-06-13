import requests
from bs4 import BeautifulSoup

req = requests.get('https://thejuneshop.com/collections/notebook-planner/products/motivational-quotes-notebook-hard-cover')

soup = BeautifulSoup(req.content,'html.parser')
price = soup.find('span',class_="ProductMeta__Price Price Price--highlight Text--subdued u-h4")
title = soup.find('h1', class_ ="ProductMeta__Title Heading u-h2")
image = soup.find_all('img')
print(title.string)
print(price.string)
print(image[2])
