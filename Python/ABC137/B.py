K, X = map(int, input().split())
start = X - K + 1
goal = X + K

ans = []
for i in range(start, goal):
    if (-1000001 < i < 1000001):
        ans.append(i)
print(*ans)
