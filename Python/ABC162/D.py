N = int(input())
S = input()

count = 0
for i in range(N):
    for j in range(i + 1, N):
        if S[i] != S[j] and (2 * j) - i <= N - 1:
            if S[(2 * j) - i] != S[i] and S[(2 * j) - i] != S[j]:
                count += 1
            else:
                continue
        else:
            continue

x = S.count("R")
y = S.count("G")
z = S.count("B")

ans = x * y * z - count
print(ans)
