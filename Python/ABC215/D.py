N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = set(range(1, M + 1))
P = set(A)
for p in A:
    i = 2
    while (i * i <= p):
        if p % i == 0:
            P.add(i)
            P.add(p // i)
        i += 1
if (1 in P):
    P.remove(1)
# print(P)

for p in P:
    k = 1
    while (k * p <= M):
        if (k * p in ans):
            ans.remove(k * p)
        k += 1

print(len(ans))
for a in ans:
    print(a)
