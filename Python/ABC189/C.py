N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    count = -1
    for j in range(i, N):
        if (A[i] <= A[j]):
            count += 1
        else:
            break
    for j in range(i, -1, -1):
        if (A[i] <= A[j]):
            count += 1
        else:
            break
    S = A[i] * count
    if (ans < S):
        ans = S
    # print(count)
    # print(S)
print(ans)
