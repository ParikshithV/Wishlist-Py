import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.urbanladder.com/products/puco-seat-cushions-set-of-2?sku=ACCSRC51RT10004&src=locations-home-decor')

soup = BeautifulSoup(req.content,'html.parser')
price = soup.find('div',class_="price discounted-price")
name = soup.find('h1', class_ ="product-title")
image = soup.find_all('img')
print(title.string)
print(price.string)
print(image[2])
