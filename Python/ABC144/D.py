import math

a, b, x = map(int, input().split())

if ((a ** 2) * b <= 2 * x):
    # (2 * b - a * math.tan(ans)) * (a ** 2) / 2 = x
    ans = math.atan(float((2 * b - (2 * x / (a ** 2))) / a))
else:
    # ((b ** 2) * a) / (2 * math.tan(ans)) = x
    ans = math.atan(float(((b ** 2) * a) / (2 * x)))
print(math.degrees(ans))
