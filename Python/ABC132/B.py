n = int(input())
p = list((map(int, input().split())))

ans = 0
a = p[0]
b = p[1]
for i in range(n - 2):
    c = p[2 + i]
    if (a < b):
        if (b < c):
            ans += 1
    else:
        if (b > c):
            ans += 1
    a = b
    b = c

print(ans)
