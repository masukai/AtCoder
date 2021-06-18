import collections

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)
s = sum([v * (v - 1) // 2 for v in c.values()])

for Ai in A:
    print(s - c[Ai] + 1)
