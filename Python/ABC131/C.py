def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b, c, d = map(int, input().split())
lcm = (c * d) // gcd(c, d)
double = b // lcm - (a - 1) // lcm
c_cnt = b // c - (a - 1) // c
d_cnt = b // d - (a - 1) // d
sub = c_cnt + d_cnt - double
print(b - a + 1 - sub)
