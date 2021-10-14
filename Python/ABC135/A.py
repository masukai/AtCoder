A, B = map(int, input().split())

ans = (A + B) / 2
if (int(ans) == ans):
    print(int(ans))
else:
    print("IMPOSSIBLE")
