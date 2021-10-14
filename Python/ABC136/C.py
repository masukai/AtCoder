N = int(input())
H = list(map(int, input().split()))

Frag = True
for i in range(N - 1):
    if (H[i] < H[i + 1]):
        H[i + 1] -= 1
    if (H[i + 1] - H[i] < 0):
        Frag = False
        break

if (Frag):
    print("Yes")
else:
    print("No")
