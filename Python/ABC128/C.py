import itertools


N, M = map(int, input().split())
s = []
k = []
for i in range(M):
    buff = list(map(int, input().split()))
    k.append(buff[0])
    s.append(buff[1:])
p = list(map(int, input().split()))
# print(k)
# print(s)
# print(p)

bin01 = [0, 1]
ans = 0
for combi in itertools.product(bin01, repeat=N):
    # print(combi)
    check = 0
    for i in range(M):
        count = 0
        for j in range(k[i]):
            if (combi[s[i][j] - 1] == 1):
                count += 1
        if (count % 2 == p[i]):
            check += 1
    if (check == M):
        ans += 1

print(ans)
