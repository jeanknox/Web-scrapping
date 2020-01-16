from requests import get
from bs4 import BeautifulSoup

url = get("https://sslproxies.org/")
soup = BeautifulSoup(url.text, "lxml")

proxys = []
for element in soup.find_all("tr")[0:30]:
    try:
        infos = element.find_all("td")
        ip = infos[0].text
        port = infos[1].text
        proxy = ip + ":" + port
        proxys.append({"https": proxy})
    except:
        pass
print(proxys)
