from collections import Counter
N = int(input())
s = [''.join(sorted(input())) for _ in range(N)]
check = Counter(s)

count = 0
for i in check.values():
    count += (i * (i - 1)) // 2  # int
print(count)
