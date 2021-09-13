import bisect


N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print(A)

B = [A[0] - 1]
for i in range(N - 1):
    B.append(A[i + 1] - A[i] + B[i] - 1)
# print(B)

K = []
for _ in range(Q):
    K.append(int(input()))

for k in K:
    if (B[-1] < k):
        print(A[-1] + k - B[-1])
    else:
        ind = bisect.bisect_left(B, k)
        print(A[ind] - 1 - (B[ind] - k))
