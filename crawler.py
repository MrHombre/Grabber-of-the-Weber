import requests
from bs4 import BeautifulSoup

r = requests.git("http://www.theatlantic.com/")

soup = BeautifulSoup(r.content)