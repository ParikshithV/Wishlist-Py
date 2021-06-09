import requests
from bs4 import BeautifulSoup
req = requests.get('https://perfumepapa.in/collections/shop-for-men/products/calvin-klein-ck-one-men')
soup = BeautifulSoup(req.content,'html.parser')
price = soup.find('span', class_ = "product-single__price on-sale")
name = soup.find('h1', class_ = "product-single__title ")
image = soup.find_all('img')

print(title.string)
print(price.string)
print(image[2])
