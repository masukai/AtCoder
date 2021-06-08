import numpy as np

N = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)

wa = np.tril(np.array([l]) + np.array([l]).T, k=-1)

count = 0
for i in range(len(l) - 2):
    count += np.sum(np.where(wa[:, i + 1:] > l[i], 1, 0))

print(count)
