N = int(input())
a = list(map(int, input().split()))

keta = len(bin(max(a))[2:])
bin_a = [bin(i)[2:].zfill(keta) for i in a]
status = []
for i in range(keta):
    buff = 0
    for bin_i in bin_a:
        buff += int(bin_i[i])
    status.append(buff)

ans = []
for bin_i in bin_a:
    bin_ans = 0
    for i in range(keta):
        buff = status[i] - int(bin_i[i])
        if (buff % 2 == 1):
            bin_ans += 10 ** (keta - (i + 1))
    ans.append(int(str(bin_ans), base=2))
print(*ans)
