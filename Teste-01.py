from bs4 import BeautifulSoup
from urllib.request import urlparse
from urllib.request import urlopen
import re

url = "https://proesi.com.br/robotica/modulos.html"
html = urlopen(url)
soup = BeautifulSoup(html, "lxml")

for element in soup.find_all("div", {"class":"infobox"}):

        print("{} : {}".format(element.find("h2",{"class" : "product-name"}).text,
                             element.find("span", {"class": "boletoBox priceAvista"}).find(
                                 "span",{"class":"price"}).text))

