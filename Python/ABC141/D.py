import heapq as hp

N, M = map(int, input().split())
A = list(map(lambda x: int(x) * -1, input().split()))
# print(A)

hp.heapify(A)
for i in range(M):
    tmp = 0
    tmp = hp.heappop(A)
    hp.heappush(A, -(-tmp // 2))
    # print(A)
print(-1 * sum(A))
