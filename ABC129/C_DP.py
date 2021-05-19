N, M = map(int, input().split())
mod = 10 ** 9 + 7

dp = [0] * (N + 1)
broken = [False] * (N + 1)
dp[0] = 1
broken[0] = True
for _ in range(M):
    a = int(input())
    broken[a] = True
if not broken[1]:
    dp[1] = 1

for i in range(2, N + 1):
    if not broken[i]:
        dp[i] = dp[i - 1] + dp[i - 2]

# print(broken)
# print(dp)
print(dp[N] % mod)
