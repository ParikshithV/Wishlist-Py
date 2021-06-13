import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.home4u.in/collections/barware-accessories/products/richmond-hip-flask-tobacco')

soup = BeautifulSoup(req.content,'html.parser')
price = soup.find('span',id="ProductPrice-6751746064539")
name = soup.find('h1', class_ ="h2 product-single__title")
image = soup.find_all('img')
print(name.string)
print(price.string)
print(image[1])
