N, M = map(int, input().split())

L_ = 1
R_ = N
for _ in range(M):
    L, R = map(int, input().split())
    if (L_ < L):
        L_ = L
    if (R_ > R):
        R_ = R

ans = R_ - L_ + 1
if (ans < 0):
    print(0)
else:
    print(ans)
