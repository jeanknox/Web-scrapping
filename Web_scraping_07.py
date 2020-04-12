from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random


pages = set()
random.seed(datetime.datetime.now())


def getInternalLinks(bs, includeUrl):
    includeUrl = "{}://{}".format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []

    for link in bs.find_all("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                if link.attrs["href"].startswith("/"):
                    internalLinks.append(includeUrl+link.attrs["href"])
                else:
                    internalLinks.append(link.attrs["href"])
    return internalLinks

def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    for link in bs.find_all("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        intenalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Randon external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)


allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):


    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme, urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')
    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            print(link) 
            getAllExternalLinks(link)


while len(allIntLinks+ allExtLinks) < 200:
    allIntLinks.add("https://g1.globo.com")
    getAllExternalLinks("https://g1.globo.com")
with open('arquivo', 'w') as arquivo:
    for i in allIntLinks:
        arquivo.write(i)
    for i in allExtLinks:
        arquivo.write(i)