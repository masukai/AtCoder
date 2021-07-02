import collections


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC = [list(map(int, input().split())) for l in range(Q)]

sumA = sum(A)
infoA = collections.Counter(A)
for rBC in BC:
    sumA += (rBC[1] - rBC[0]) * infoA[rBC[0]]
    print(sumA)
    infoA[rBC[1]] += infoA[rBC[0]]
    infoA[rBC[0]] = 0
    # print(infoA)
