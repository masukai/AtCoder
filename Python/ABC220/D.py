N = int(input())
A = list(map(int, input().split()))

mod = 998244353

dp = []
dp = [[0] * 10 for i in range(N)]

for i in range(10):
    if (A[0] == i):
        dp[0][i] = 1

for i in range(1, N):
    for j in range(10):
        if (dp[i - 1][j] > 0):
            dp[i][(j * A[i]) % 10] += dp[i - 1][j]
            dp[i][(j * A[i]) % 10] %= mod
            dp[i][(j + A[i]) % 10] += dp[i - 1][j]
            dp[i][(j + A[i]) % 10] %= mod

for i in range(10):
    print(dp[N - 1][i])
# print(dp)
