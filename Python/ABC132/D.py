import math


N, K = map(int, input().split())

mod = 10 ** 9 + 7
set = math.factorial((N - K) + 1) * math.factorial(K - 1)
for i in range(K):
    if (i > N - K):
        print(0)
    else:
        U = math.factorial((N - K) - i) * math.factorial(i + 1) * math.factorial((K - 1) - i) * math.factorial(i)
        ans = set // U
        print(ans % mod)
