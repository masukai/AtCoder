N, M = map(int, input().split())


class UnionFind:
    def __init__(self, n):
        self.root = [-1] * n

    def find(self, x):
        if self.root[x] < 0:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.root[x] > self.root[y]:
            x, y = y, x
        self.root[x] += self.root[y]
        self.root[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.root[self.find(x)] * -1


union = UnionFind(N)
for i in range(M):
    A, B = map(int, input().split())
    union.unite(A - 1, B - 1)
    # print(union.root)  # 小さい値ほど親

print(-min(union.root))
