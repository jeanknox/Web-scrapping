from requests import get
from bs4 import BeautifulSoup
import datetime
import csv
import time
import sys
import os

def busca_views():
    url = get("https://www.youtube.com/watch?v=WuYCXPfHdZk")
    soup = BeautifulSoup(url.text, "lxml")
    quantidade_views = soup.find("div", attrs={"class":"watch-view-count"}).text.replace("visualizações","")
    print(quantidade_views+"Visualizacoes")
    dia_e_hora = datetime.datetime.now()
    current_date = dia_e_hora.strftime("%d/%m/%Y %H:%M")
    print(current_date)
    with open("Lista_views.csv", "a+") as lista:
        colunas = ["Data","Quantidade de Views"]
        writer = csv.DictWriter(lista, fieldnames=colunas,delimiter=";")
        writer.writerow({"Data":dia_e_hora, "Quantidade de Views": quantidade_views})

while True:
    busca_views()
    for i in range(60,0,-1):
        sys.stdout.flush()
        os.system("cls")
        print("Proxima busca em:" + str(i)+ "S")
        time.sleep(1)
