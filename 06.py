from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("https://docs.python.org/3/library/urllib.request.html#module-urllib.request")

bs = BeautifulSoup(url.read(), "html.parser")
print(bs.a)
