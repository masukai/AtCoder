s = list(input())


def cal(set):
    r = set.count("R")
    l = set.count("L")
    rset = [0] * (r + l)
    rset[r - 1] = (r - 1) // 2 + l // 2 + 1
    rset[r] = r // 2 + (l - 1) // 2 + 1
    return rset


s += "R"
set = ""
ans = []
for i in range(len(s) - 1):
    set += s[i]
    if ((s[i] == 'L') & (s[i + 1] == 'R')):
        ans.extend(cal(set))
        set = ""

print(*ans)
