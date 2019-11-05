from urllib.request import  urlopen
from bs4 import  BeautifulSoup

url = "http://www.pythonscraping.com/pages/warandpeace.html"
html = urlopen(url)
bs = BeautifulSoup(html.read(), "html.parser")

namelist = bs.find_all("span",{"class":"green"})

for name in namelist:
    print(name)
