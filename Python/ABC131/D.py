N = int(input())
AB = [list(map(int, input().split())) for AB in range(N)]

AB_sort = sorted(AB, key=lambda x: x[1])

S = 0
frag = True
for i in range(N):
    S += AB_sort[i][0]
    if (S > AB_sort[i][1]):
        print("No")
        frag = False
        break

if (frag):
    print("Yes")
