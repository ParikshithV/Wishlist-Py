import requests
from bs4 import BeautifulSoup

req = requests.get('https://streetstylestore.com/index.php?id_product=61561&controller=product')

soup = BeautifulSoup(req.content,'html.parser')
price = soup.find('span',id="our_price_display")
title = soup.find('h2', class_ = "product-name")
image = soup.find_all('img')
print(title.string)
print(price.string)
print(image[2])
