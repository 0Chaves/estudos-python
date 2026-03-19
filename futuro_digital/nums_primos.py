import numpy as np

primos = np.array([2])
dados = np.arange(3,1000)


for i in dados:
    primo = True
    for n in primos:
        res = i%n
        if(res == 0):
            primo = False
            break
    if(primo):
        primos = np.append(primos, i)

print(primos)