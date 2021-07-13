N = int(input())
C = list(input())

search = len(C) - 1
ans = 0
Frag = False
for i in range(len(C)):
    if (i >= search):
        break
    if (C[i] == "W"):
        for j in range(search, i, -1):
            if (C[j] == "R"):
                C[i], C[j] = C[j], C[i]
                search = j - 1
                ans += 1
                Frag = False
                break
            else:
                Frag = True
    if (Frag):
        break
    # print(C)
print(ans)
