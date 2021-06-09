import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.nike.com/in/t/mercurial-superfly-8-elite-fg-football-boot-24FtzR/CV0958-403')
soup = BeautifulSoup(req.content,'html.parser')
price = soup.find('div',class_="product-price css-11s12ax is--current-price")
name = soup.find('h1', id = "pdp_product_title")
image = soup.find_all('img')
print(name.string)
print(price.string)
print(image[2])
