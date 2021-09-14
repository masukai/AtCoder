S = list(input())
mod = 10 ** 9 + 7
name = ["c", "h", "o", "k", "u", "d", "a", "i"]
S = [i for i in S if i in name]

count = [0] * len(name)
for i in range(len(S)):
    n = 0
    for j in range(len(name)):
        n = j
        if (S[i] == name[j]):
            break
    if (n == 0):
        count[0] += 1
    else:
        count[j] += count[j - 1]
    # print(i, count)

print(count[-1] % mod)
