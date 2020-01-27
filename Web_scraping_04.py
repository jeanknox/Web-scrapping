from bs4 import BeautifulSoup
from requests import get
import re

url = get("http://en.wikipedia.org/wiki/Kevin_Bacon")
soup = BeautifulSoup(url.text, "html.parser")
for link in soup.find("div", {"id": 
    "bodyContent" }).find_all("a", {"href":re.compile(r"^(/wiki/)((?!:).)*$")}):
    if "href" in link.attrs:
        print(link.attrs["href"])
