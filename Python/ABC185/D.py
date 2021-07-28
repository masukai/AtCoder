N, M = map(int, input().split())
A = list(map(int, input().split()))


def solve(N, M, A):
    A.append(0)
    A = sorted(A)
    A.append(N + 1)
    # print(A)

    diff_A = []
    min_A = 10 ** 9 + 1
    for i in range(M + 1):
        buff = A[i + 1] - A[i] - 1
        if (buff != 0):
            diff_A.append(buff)
            if (buff < min_A):
                min_A = buff
    # print(diff_A)
    # print(min_A)
    if (min_A == 10 ** 9 + 1):
        return 0
    else:
        count = 0
        for Ai in diff_A:
            count += Ai // min_A
            if (Ai % min_A > 0):
                count += 1
        return count


if (M == 0):
    print(1)
else:
    ans = solve(N, M, A)
    print(ans)
