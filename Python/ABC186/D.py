N = int(input())
A = list(map(int, input().split()))

A = sorted(A)

buff = []
for i in range(N // 2):
    if (N % 2 == 0):
        buff.append(1 + 2 * i)
    else:
        buff.append(2 * (i + 1))
mul = []
for i in buff[::-1]:
    mul.append(i * -1)
if (N % 2 == 1):
    mul.append(0)
for i in buff:
    mul.append(i)

S = 0
for i in range(N):
    S += A[i] * mul[i]
print(S)
