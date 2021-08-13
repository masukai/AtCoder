N, M = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for BC in range(M)]
# A.sort()
BC.sort(key=lambda x: (x[1], x[0]), reverse=True)

C = []
count = 0
for BCj in BC:
    for i in range(BCj[0]):
        C.append(BCj[1])
        count += 1
        if (count > N):
            break
    if (count > N):
        break
A = A + C
A.sort()

print(sum(A[-N:]))
