import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = np.array([1,2,3,4])
print(f"{a}")
print(type(a))

valor = np.random.randint(0,10,(3,4))
print(f"{valor}\n")
print("-------------------------")
valor2 = valor.reshape(4,3)
print(f"{valor2}\n\n\n")

# "antes de verificar a média, deve-se verificar o desvio padrão"
# quanto mais proximo de 0 for o desvio padrão, mais homogeneo são os dados e proximos da média
# dados heterogeneos e dispersos aumentam o valor do desvio padrão
notas = np.array([10, 3, 2, 9.4, 6.7])
desvio = np.std(notas)
print(f"{desvio}\n\n\n")


#Uma Serie sempre tem um valor e indice, que é o momento do dado. Poderia ser utilizado para calcular uma temperatura a cada hora, por exemplo
serie = pd.Series([10,20,40,30,50,90])
print(f"{serie}\n")
s = pd.Series([10,20,30,40], index=["a","b","c","c"])
print(f"{s}\n")
# TODO: se buscar pelo indice, vai buscar todos que tem o mesmo indice buscado


#cada item aqui é um Series. "nome" é um Series. "nota" é um Series
#e com isso "dados" é um DataFrame
dados = {
    "nome" : ["João", "Maria", "Jose"],
    "nota" : [8.5, 7, 9.2]
}
df = pd.DataFrame(dados)
print(f"{df}\n")

df.info()
#25% é o primeiro quarter, 50% segundo quarter e 75% o terceiro
print(df.describe())