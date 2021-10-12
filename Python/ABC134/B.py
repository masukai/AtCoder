N, D = map(int, input().split())

if (N % (2 * D + 1) > 0):
    a = 1
else:
    a = 0
print(N // (2 * D + 1) + a)
