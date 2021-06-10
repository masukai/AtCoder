A, B, X = map(int, input().split())


def check(x):
    return A * x + B * len(str(x))


min = 0
max = 1000000001
while min + 1 != max:
    md = (min + max) // 2
    if check(md) <= X:
        min = md
    else:
        max = md

print(min)
