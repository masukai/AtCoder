import itertools


N, M = map(int, input().split())
AB = [list(map(int, input().split())) for l in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for l in range(K)]

buff = 0
ans = 0
# 二つのうちどちらを取るか (2 ** 16)
for combi in itertools.product(*CD):
    buff = 0
    for a, b in AB:
        if ((a in combi) and (b in combi)):
            buff += 1
    if (buff > ans):
        ans = buff

print(ans)
