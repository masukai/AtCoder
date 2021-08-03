n = int(input())
l = [1, 1]

for _ in range(n):
    if (input() == "AND"):
        l[0] += sum(l)
    else:
        l[1] += sum(l)

print(l[1])
