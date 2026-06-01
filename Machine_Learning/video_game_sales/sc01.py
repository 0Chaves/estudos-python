import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Carregar os dados na memoria
df = pd.read_csv("dataset/Video_Games_Sales_1980-2024_Raw.csv")

#Excluir coluna de imagem que não será utilziada
del df['img']

df.info()
