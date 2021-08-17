H, W = map(int, input().split())


G = ['#' * (W + 2)]
for i in range(H):
    G.append('#' + input() + '#')
G.append('#' * (W + 2))

d1 = [[0] * (W + 2) for _ in range(H + 2)]
d2 = [[0] * (W + 2) for _ in range(H + 2)]


def cal(G, d, X, Y, cond):
    for i in range(1, X + 1):
        akari = 0
        for j in range(1, Y + 2):
            if (cond is False):
                j, i = i, j
            if G[i][j] == '.':
                akari += 1
            elif G[i][j] == '#' and akari > 0:
                if (cond is True):
                    d[i][j - 1] = akari
                else:
                    d[i - 1][j] = akari
                akari = 0
            if (cond is False):
                j, i = i, j
        for j in range(Y, 0, -1):
            if (cond is False):
                j, i = i, j
            if d[i][j] > 0:
                akari = d[i][j]
            if G[i][j] == '.' and d[i][j] == 0:
                d[i][j] = akari
            if (cond is False):
                j, i = i, j
    return d


d1 = cal(G, d1, H, W, True)
d2 = cal(G, d2, W, H, False)

ans = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        ans = max(ans, d1[i][j] + d2[i][j])
print(ans - 1)
