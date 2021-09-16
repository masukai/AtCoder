H, W, N = map(int, input().split())

A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

Xdict = {x: i + 1 for i, x in enumerate(sorted(list(set(A))))}
Ydict = {y: i + 1 for i, y in enumerate(sorted(list(set(B))))}
# print(Xdict)
# print(Ydict)

for i in range(N):
    print(Xdict[A[i]], Ydict[B[i]])
