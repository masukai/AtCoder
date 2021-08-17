import numpy as np


H, W = map(int, input().split())

status = []
for i in range(H + 1):
    if (i == H):
        S = ["#"] * W
    else:
        S = list(input())
    S.append("#")
    status.append(S)
# print(status)


def check(set, max_):
    num = []
    for Si in set:
        buff = []
        count = 0
        for j in range(max_ + 1):
            if (Si[j] == "#"):
                if (count == 0):
                    buff.append(0)
                else:
                    buff.extend([count] * count)
                    buff.append(0)
                count = 0
            else:
                count += 1
        num.append(buff[:-1])
    # print(num[:-1])
    return np.array(num[:-1])


ans1 = check(status, W)
ans2 = check(np.array(status).T, H)
print(ans1 + ans2.T - 1)
print(np.max(ans1 + ans2.T - 1))
