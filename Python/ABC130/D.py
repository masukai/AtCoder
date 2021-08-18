N, K = map(int, input().split())
a = list(map(int, input().split()))


def check(A):
    ans = 0
    buff = 0
    count = 0
    for i in range(N):
        buff += A[i]
        while (buff >= K):
            ans += N - i
            buff -= A[count]
            count += 1
    return ans


ans = check(a)
print(ans)
