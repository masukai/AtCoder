X = int(input())

Arange = 1000
Brange = 1000

for i in range(Arange):
    Z = (i ** 5) - X
    for j in range(Brange * (-1), Brange):
        frag = False
        if (j ** 5 == Z):
            frag = True
            break
        # print("{0} {1}".format(i, j))
    if (frag):
        break
print("{0} {1}".format(i, j))
