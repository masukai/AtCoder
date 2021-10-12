N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
A_max = max(A)
B = sorted(A)[-2]

for i in range(N):
    if (A_max > A[i]):
        print(A_max)
    else:
        print(B)
