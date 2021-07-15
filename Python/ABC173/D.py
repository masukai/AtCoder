N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
# print(A)

ans = 0
count = 0
for i in range(N):
    ans += A[count]
    if (i % 2 == 1):
        count += 1

print(ans - A[0])
