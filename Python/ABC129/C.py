import sys
sys.setrecursionlimit(10 ** 8)  # 再帰関数の限界


def f(k, bn=1, bn1=2):
    if (k < 0):
        return 0
    elif (k == 0 or k == 1):
        return bn
    elif (k == 2):
        return bn1
    else:
        return f(k - 1, bn1, bn + bn1)


N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]
a.append(N + 1)
set = []
start = 0
for i in a:
    set.append(f(i - 1 - start))
    start = i + 1

ans = 1
for i in set:
    ans *= i
    if (ans > 1000000007):
        ans %= 1000000007
print(ans)
