N = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(N):
    if (p[i] - (i + 1) == 0):
        count += 1
if (N - count > 2):
    print("NO")
else:
    print("YES")
