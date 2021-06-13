import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.berrylush.com/collections/dresses/products/dr299yl-yellow-floral-print-shoulder-strap-dress')
soup = BeautifulSoup(req.content,'html.parser')
price = soup.find('span', class_ = "money")
title = soup.find('h1', class_ = "product_name")
image = soup.find('img',0)

print(title.string)
print(price.string)
print(image)
