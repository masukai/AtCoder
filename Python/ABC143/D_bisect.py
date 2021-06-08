import bisect

N = int(input())
l = list(map(int, input().split()))

l.sort()

count = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        count += bisect.bisect_left(l, l[i] + l[j]) - (j + 1)
print(count)

# ex    2 3 4 5 6
# index 0 1 2 3 4
