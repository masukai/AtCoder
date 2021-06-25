import itertools

N, M, X = map(int, input().split())
A = [list(map(int, input().split())) for l in range(N)]

ans = float('inf')
com = [l for l in range(N)]
for i in com:
    com_list = list(itertools.combinations(com, N - i))
    # print(com_list)
    for tuple in com_list:
        check = [0] * (M + 1)
        for j in range(len(tuple)):
            for k in range(M + 1):
                check[k] += A[tuple[j]][k]
        frag = 0
        for k in range(M):
            if (check[k + 1] >= X):
                frag += 1
        if ((frag == M) and (ans > check[0])):
            ans = check[0]
if (ans == float('inf')):
    ans = -1

print(int(ans))
