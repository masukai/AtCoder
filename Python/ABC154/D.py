N, K = map(int, input().split())
p = list(map(int, input().split()))


ans_max = 0
for i in range(K):
    ans_max += p[i]

check = ans_max
for i in range(N - K):
    check = check - p[i] + p[i + K]
    if (check > ans_max):
        ans_max = check

print(ans_max / 2.0 + 0.5 * K)
