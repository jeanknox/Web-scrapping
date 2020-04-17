from bs4 import BeautifulSoup
from urllib.request import urlparse
from urllib.request import urlopen
from requests import get
import re
from random import choice

url = "https://proesi.com.br/"

internal_urls = []
external_urls = []

def get_soup(url):
    html = get(url)
    soup = BeautifulSoup(html.text, "lxml")
    return soup

def busca_links(soup):
    for elemento in soup.find_all("a",{"href": re.compile(
            r"((http|ftp|https)://)?([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")}):
        if "href" in elemento.attrs:
            if "https://proesi.com.br" in elemento.attrs["href"]:
                if elemento.attrs["href"] not in internal_urls:
                    internal_urls.append(elemento.attrs["href"])

            if "https://proesi.com.br" not in elemento.attrs["href"]:
                if elemento.attrs["href"] not in external_urls:
                    external_urls.append(elemento.attrs["href"])
            print(elemento.attrs["href"])

def links_internos(start_link):
    while len(internal_urls) < 1000:
        internal_urls.append(start_link)
        domain = choice(internal_urls)
        busca_links(get_soup(domain))
        print(len(internal_urls))
    with open("Domains.txt", "w") as domains:
        for i in internal_urls:
            domains.write(i)
            domains.write("\n")


links_internos(url)



# for element in soup.find_all("div", {"class":"infobox"}):

        # print("{} : {}".format(element.find("h2",{"class" : "product-name"}).text,
        #                      element.find("span", {"class": "boletoBox priceAvista"}).find(
                                 # "span",{"class":"price"}).text))

