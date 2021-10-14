N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if (B[-1] > A[-1]):
    A = list(reversed(A))
    B = list(reversed(B))

sumA = sum(A)
for i in range(N):
    if (B[i] - A[i] >= 0):
        buff = B[i] - A[i]
        A[i] = 0
    else:
        buff = 0
        A[i] -= B[i]
    A[i + 1] -= buff
    if (A[i + 1] < 0):
        A[i + 1] = 0
# print(A)
print(sumA - sum(A))
