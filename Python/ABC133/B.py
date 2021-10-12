import math

N, D = map(int, input().split())

X = []
for _ in range(N):
    buff = list(map(int, input().split()))
    X.append(buff)

c = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        ans = 0
        for k in range(D):
            ans += (X[i][k] - X[j][k]) ** 2
        if (math.sqrt(ans) == int(math.sqrt(ans))):
            c += 1
print(c)
