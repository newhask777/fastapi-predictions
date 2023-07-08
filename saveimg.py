import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/home'

res = requests.get(url)

print(res)

with open('imgs.jpg', 'w') as f:
    f.write(str(res))