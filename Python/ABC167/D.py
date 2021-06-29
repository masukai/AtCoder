N, K = map(int, input().split())
A = list(map(int, input().split()))

G = [0] * (N + 1)
G[0] = 1
counter = [0] * N
counter[0] = 1
now = 1
for i in range(N + 1):
    now = A[now - 1]
    G[i + 1] = now
    counter[now - 1] += 1
    if (counter[now - 1] == 2):
        break

shiftG = G.index(now)
loopG = G[G.index(now):i + 1]
# print(G)
# print(shiftG)
# print(loopG)
if (K > shiftG):
    ans = (K - shiftG) % len(loopG)
    print(loopG[ans])
else:
    print(G[K])
