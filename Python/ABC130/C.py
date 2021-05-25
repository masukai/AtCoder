W, H, x, y = map(int, input().split())

frag = 0
if (W / 2 == x and H / 2 == y):
    frag = 1

print((W * H) / 2, frag)
