N, X = map(int, input().split())
L = list(map(int, input().split()))

D = 0
count = 1
for Li in L:
    D += Li
    if (D <= X):
        count += 1
    else:
        break
print(count)
