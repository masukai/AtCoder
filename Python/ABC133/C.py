L, R = map(int, input().split())

S = 2019

if ((R // S) - (L // S) > 0):
    print(0)
else:
    min_ = 2018
    start = L % S
    end = R % S + 1
    for i in range(start, end):
        for j in range(i + 1, end):
            if ((i * j) % S < min_):
                min_ = (i * j) % S
    print(min_)
