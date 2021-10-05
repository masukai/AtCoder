N = int(input())
a = []
for i in range(N):
    S, P = input().split()
    P = int(P)
    a.append([S, -P, i + 1])
a.sort()
for a_ in a:
    print(a_[2])
