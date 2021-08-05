N = int(input())

M = int(N ** 0.5) + 1

count = 0
for i in range(1, M):
    if (N % i == 0):
        if (((2 * N // i + 1 - i) % 2 == 0)):
            count += 2
        j = N // i
        if ((j != i) and ((2 * N // j + 1 - j) % 2 == 0)):
            count += 2
    # print(i, count)
print(count)
