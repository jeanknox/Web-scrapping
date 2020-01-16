from bs4 import BeautifulSoup
from requests import get
import re

url = get("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(url.text, "html.parser")
images = soup.find_all("img", {"src": re.compile(r"\.\.\/img\/gifts\/[a-zA-z0-9]+\.jpg")})
for image in images:
    print(image)
