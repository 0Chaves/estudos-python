import numpy as np

seq_fibonacci = np.array([0,1])

for i in range(0, 10):
    prox = seq_fibonacci[-1] + seq_fibonacci[-2]
    seq_fibonacci = np.append(seq_fibonacci, prox)

print(seq_fibonacci)