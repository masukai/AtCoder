N, M = map(int, input().split())
sc = [list(map(int, input().split())) for sc in range(M)]

num = ["A"] * N
counter = [0] * N
ans = 0
for i in range(M):
    if (num[sc[i][0] - 1] != sc[i][1]):
        if (counter[sc[i][0] - 1] < 1):
            num[sc[i][0] - 1] = sc[i][1]
            counter[sc[i][0] - 1] += 1
        else:
            ans = -1
            break
    else:
        continue

for i in range(N):
    if (num[i] == "A"):
        if ((i == 0) and (N > 1)):
            num[i] = 1
        else:
            num[i] = 0

if (ans != -1):
    check = int(''.join(map(str, num)))
    if (len(str(check)) == N):
        ans = check
    else:
        ans = -1

print(ans)
