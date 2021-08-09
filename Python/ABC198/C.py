R, X, Y = map(int, input().split())

dist = (X ** 2 + Y ** 2) ** 0.5
if (dist < R):
    ans = 2
else:
    ans = int(dist // R)
    if ((dist / R) > ans):
        ans += 1
print(ans)
