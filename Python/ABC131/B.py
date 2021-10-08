N, L = map(int, input().split())

ans = []
for i in range(N):
    ans.append(L + i)

if (min(ans) > 0):
    print(sum(ans) - min(ans))
elif (max(ans) < 0):
    print(sum(ans) - max(ans))
else:
    print(sum(ans))
