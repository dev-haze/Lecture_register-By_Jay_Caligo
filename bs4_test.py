from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.google.com"
html = urlopen(url)
#obj = BeautifulSoup(html, "html.parser")

#print(obj.head.title)

