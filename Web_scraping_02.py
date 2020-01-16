from bs4 import BeautifulSoup
from requests import get

url = get("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(url.text, "html.parser")

for child in soup.find("table",{"id":"giftList"}).children:
    print(child)
