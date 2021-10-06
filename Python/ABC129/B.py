N = int(input())
W = list(map(int, input().split()))
S = sum(W)

ans = []
for i in range(N):
    S -= 2 * W[i]
    ans.append(abs(S))

print(min(ans))
