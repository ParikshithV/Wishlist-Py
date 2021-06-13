import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.koovs.com/koovs-womens-tshirts-150582-167800.html')
soup = BeautifulSoup(req.content,'html.parser')
price = soup.find('span',class_="pd-price")
title = soup.find('div', class_ = "product-name")
image = soup.find_all('img')
print(title.string)
print(price.string)
print(image[2])
