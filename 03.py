from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import  HTTPError
from urllib.error import  URLError

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    print("Sucess!")
