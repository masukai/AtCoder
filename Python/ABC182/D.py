N = int(input())
A = list(map(int, input().split()))

ans = now = buff = set = 0
for i in range(N):
    buff += A[i]
    set = max(set, buff)
    ans = max(ans, now + set)
    now += buff
print(ans)
