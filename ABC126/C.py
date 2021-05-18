import numpy as np

N, K = map(int, input().split())
Nset = np.arange(1, N + 1)
Lset = np.ceil(np.log2(K) - np.log2(Nset))
Lset[Lset < 0] = 0
print(sum((1 / 2) ** Lset) / N)
