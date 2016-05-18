import requests
from bs4 import BeautifulSoup

url = "http://www.theatlantic.com/" # Only for learning purposes, please don't use data without approval
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
    if "http" in link.get("href"):
        print "<a href='%s'>%s</a>" %(link.get("href"), link.text)


g_data = soup.find_all("div",{"class": "content"})
