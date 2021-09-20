N = int(input())
xy = [list(map(int, input().split())) for xy in range(N)]
xy_set = set()
for x, y in xy:
    xy_set.add((x, y))

xy = sorted(xy)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if ((xy[i][0] < xy[j][0] and xy[i][1] < xy[j][1]) and ((xy[i][0], xy[j][1]) in xy_set) and ((xy[j][0], xy[i][1]) in xy_set)):
            ans += 1

print(ans)
