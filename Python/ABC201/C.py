S = input()
a = S.count('o')
b = S.count('x')
c = S.count('?')

if ((a >= 5) or (b == 10)):
    print(0)
elif (a == 0):
    print(c ** 4)
elif (a == 1):
    print(4 * (c ** 3) + 6 * (c ** 2) + 4 * c + 1)
elif (a == 2):
    print(12 * (c ** 2) + 24 * c + 14)
elif (a == 3):
    print(24 * c + 36)
elif (a == 4):
    print(24)
