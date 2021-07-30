N = int(input())
AB = [list(map(int, input().split())) for AB in range(N)]

Asum = 0
for i in range(N):
    AB[i].append(AB[i][0] * 2 + AB[i][1])  # ?
    Asum += AB[i][0]
ABs = sorted(AB, key=lambda x: (x[2], x[0]), reverse=True)
# print(ABs)

Tsum = 0
for i in range(N):
    Tsum += ABs[i][2] - ABs[i][0]  # ?
    Asum -= ABs[i][0]
    # print(Tsum)
    # print(Asum)
    if (Tsum > Asum):
        print(i + 1)
        break
