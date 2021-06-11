N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

for i in range(len(T) - K):
    if (T[i] == T[i + K]):
        if (i < len(T) - K - 1):
            T = T[:i + K] + 'a' + T[i + K + 1:]
        else:
            T = T[:i + K] + 'a'

ans = 0
for i in range(len(T)):
    if (T[i] == 'r'):
        ans += P
    elif (T[i] == 's'):
        ans += R
    elif (T[i] == 'p'):
        ans += S
    else:
        ans += 0

print(ans)
