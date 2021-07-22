import itertools
import collections


S = list(str(input()))
S = [int(s) for s in S]
c = collections.Counter(S)
Sset = []
for i in c.items():
    if (i[1] > 3):
        N = 3
    else:
        N = i[1]
    for j in range(N):
        Sset.append(i[0])
# print(Sset)

if (len(Sset) == 1):
    if (Sset[0] == 8):
        print("Yes")
    else:
        print("No")
elif (len(Sset) == 2):
    buff1 = Sset[0] * 10 + Sset[1]
    buff2 = Sset[1] * 10 + Sset[0]
    if ((buff1 % 8 == 0) or (buff2 % 8 == 0)):
        print("Yes")
    else:
        print("No")
else:
    Frag = True
    for p in itertools.permutations(Sset, 3):
        buff = p[0] * 100 + p[1] * 10 + p[2]
        if (buff % 8 == 0):
            print("Yes")
            Frag = False
            break
    if (Frag):
        print("No")
