from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"

html = urlopen(url)
bs = BeautifulSoup(html.read(), "html.parser")

namelist = bs.findAll("span",{"class":"green"})
for i in namelist:
    print(i.get_text())
print(bs.h1)
print(bs.body.h1)
