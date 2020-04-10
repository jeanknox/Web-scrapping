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
                if link.attrs["href"].startswitch("/"):
                    internalLinks.append(includeUrl+link.attrs["href"])
                else:
                    internalLinks.append(link.attrs["href"])
    return internalLinks

def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    for link in bs.find_all("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:


