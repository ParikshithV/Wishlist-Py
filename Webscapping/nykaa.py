import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.nike.com/in/t/mercurial-superfly-8-elite-fg-football-boot-24FtzR/CV0958-403')
soup = BeautifulSoup(req.content,'html.parser')
price = soup.find('span',class_=" css-nt79bs e4picg41")
name = soup.find('div', class_ = "css-oumgbf e1vt4n324")
image = soup.find_all('img')
print(name)
print(price.string)
print(image[2])
