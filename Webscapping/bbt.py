import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.redwolf.in/rock-paper-scissors-lizard-spock-mug-india')
soup = BeautifulSoup(req.content,'html.parser')
price = soup.find('span',class_="no_special_price_original_price")
name = soup.find('h2', class_ = "product_title")
image = soup.find_all('img')
print(name.string)
print(price.string)
print(image[6])
