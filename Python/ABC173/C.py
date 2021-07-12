import itertools


H, W, K = map(int, input().split())
status = [list(map(str, input().split())) for l in range(H)]
add_ = ["." * W]
status.insert(0, add_)
for row in status:
    row[0] = "." + row[0]
# print(status)

Hlist = [i for i in range(1, H + 1)]
Wlist = [j for j in range(1, W + 1)]
Hresult = []
for n in range(1, len(Hlist) + 1):
    for conb in itertools.combinations(Hlist, n):
        Hresult.append(list(conb))  # タプルをリスト型に変換
Hresult.insert(0, [0])
Wresult = []
for n in range(1, len(Wlist) + 1):
    for conb in itertools.combinations(Wlist, n):
        Wresult.append(list(conb))  # タプルをリスト型に変換
Wresult.insert(0, [0])
# print(Hresult)
# print(Wresult)

max_counter = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if (status[i][0][j] == "#"):
            max_counter += 1
# print(max_counter)

ans = 0
for Hcon in Hresult:
    for Wcon in Wresult:
        counter = 0
        cross = 0
        for i in Hcon:
            for j in range(W + 1):
                if (status[i][0][j] == "#"):
                    counter += 1
        for i in range(H + 1):
            for j in Wcon:
                if (status[i][0][j] == "#"):
                    counter += 1
        for i in Hcon:
            for j in Wcon:
                if (status[i][0][j] == "#"):
                    cross += 1
        if ((max_counter - counter + cross) == K):
            # print(Hcon, Wcon)
            ans += 1

print(ans)
