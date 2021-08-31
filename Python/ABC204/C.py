import sys
sys.setrecursionlimit(10**7)


N, M = map(int, input().split())

buff = [[] for _ in range(N)]
if (M > 0):
    for i in range(M):
        A, B = map(int, input().split())
        buff[A - 1].append(B - 1)
# print(buff)


def dfs(v):
    if (check[v] is True):
        return
    else:
        check[v] = True
        for i in buff[v]:
            # print(check)
            dfs(i)


ans = 0
for i in range(N):
    check = [False] * N
    dfs(i)
    ans += sum(check)

print(ans)
