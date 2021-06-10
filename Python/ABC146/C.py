A, B, X = map(int, input().split())

if (len(str(X)) >= 10):
    x_max = 10
else:
    x_max = len(str(X))

x_range = list(range(x_max - 1, 0, -1))
ans = 0
for i in x_range:
    for j in range(10 ** i, 10 ** (i - 1), -1):
        if (X >= A * j + B * i):
            ans = j
            break
    else:
        continue
    break

if ((ans == 0) and (X >= A + B)):
    ans = 1

print(ans)
