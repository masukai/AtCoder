N = int(input())
a = list(map(int, input().split()))

ans = [0 for _ in range(N)]

for i in range(N, 0, -1):
    j = 1
    count = 0
    num = i
    while (num <= N):
        count += ans[num - 1]
        j += 1
        num = i * j
    ans[i - 1] = (count + a[i - 1]) % 2

print(sum(ans))
if (sum(ans) != 0):
    ans_num = [i + 1 for i, x in enumerate(ans) if x == 1]
    print(*ans_num)
