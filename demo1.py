import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.qyl88.com/')

demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

print(soup.prettify())