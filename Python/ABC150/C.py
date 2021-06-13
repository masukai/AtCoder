import math

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))


def f(K):
    ans = 0
    for i in range(N):
        ans += (K[i] - 1) * math.factorial(N - (i + 1))
        for j in range(i + 1, N):
            if (K[i] < K[j]):
                K[j] -= 1
    return ans


print(abs(f(P) - f(Q)))
