import itertools


N, W = map(int, input().split())

now = [0] * (2 * 10 ** 5 + 1)
for i in range(N):
    S, T, P = map(int, input().split())
    now[S] += P
    now[T] -= P

for i in itertools.accumulate(now):
    if (i > W):
        print("No")
        exit()

print("Yes")
