from collections import deque

S = deque((list(input())))
Q = int(input())

frag = True
for i in range(Q):
    L = list(map(str, input().split()))
    if (L[0] == "1"):
        if (frag):
            frag = False
        else:
            frag = True
    else:
        if (frag):
            if (L[1] == "1"):
                S.appendleft(L[2])
            else:
                S.append(L[2])
        else:
            if (L[1] == "1"):
                S.append(L[2])
            else:
                S.appendleft(L[2])

if (frag):
    print("".join(S))
else:
    rS = reversed(S)
    print("".join(rS))
