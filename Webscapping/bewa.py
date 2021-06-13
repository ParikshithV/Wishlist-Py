import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.bewakoof.com/p/navy-blue-plain-full-sleeve-round-neck-men-t-shirt')
soup = BeautifulSoup(req.content,'html.parser')
price = soup.find('span', id = "testNetProdPrice")
title = soup.find('h1', id = "testProName")
image = soup.find_all('img')

print(title.string)
print(price.string)
print(image[2])
