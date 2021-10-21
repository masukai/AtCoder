N = int(input())
A = list(map(int, input().split()))

sA = 1
for Ai in A:
    sA *= Ai
sB = 0
for Ai in A:
    sB += sA // Ai
print(sA / sB)
