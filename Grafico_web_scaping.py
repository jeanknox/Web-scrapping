import pandas as pd
import matplotlib.pyplot as plt

arquivo = pd.read_csv("Lista_views.csv", encoding="latin-1", delimiter=";")
plt.plot(arquivo["Data"],arquivo["Quantidade de Views"])
plt.xlabel("Datas")
plt.ylabel("Quantidade de Views")
plt.savefig("Histograma.png")
