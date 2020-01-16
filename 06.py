from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import get

url = get("https://docs.python.org/3/library/urllib.request.html#module-urllib.request")

bs = BeautifulSoup(url, "html.parser")
print(bs.a)
