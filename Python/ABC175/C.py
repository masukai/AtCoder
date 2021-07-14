X, K, D = map(int, input().split())

Y = X // D
if (Y < 0):
    Y = abs(Y) - 1
if (K < Y):
    if (X > 0):
        ans = X - K * D
    else:
        ans = X + K * D
else:
    K -= Y
    if (X > 0):
        buff = X - Y * D
    else:
        buff = X + Y * D
    if (K % 2 == 0):
        ans = buff
    else:
        if (X > 0):
            ans = buff - D
        else:
            ans = buff + D
print(abs(ans))
