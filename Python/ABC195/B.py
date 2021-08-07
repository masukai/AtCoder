A, B, W = map(int, input().split())

W *= 1000

max_buff = W // A
min_buff = W // B
if ((W / B) > min_buff):
    min_buff += 1
if (min_buff > max_buff):
    print("UNSATISFIABLE")
else:
    print(min_buff, max_buff)
