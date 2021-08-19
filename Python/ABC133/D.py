N = int(input())
A = list(map(int, input().split()))

x1 = 0
for i in range(N):
    if (i % 2 == 0):
        x1 += A[i]
    else:
        x1 -= A[i]

x = [x1]
buff = x1
for i in range(N - 1):
    buff = 2 * A[i] - buff
    x.append(buff)

print(*x)
