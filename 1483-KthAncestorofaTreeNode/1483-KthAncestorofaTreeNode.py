# Last updated: 28/4/2025, 6:52:36 pm
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.logs = []

        i = 1
        m = 0
        while i <= n:
            self.logs.append(defaultdict(lambda: -1))
            i *= 2
            m += 1

        for node in range(1, n):
            self.logs[0][node] = parent[node]

        for k in range(1, m):
            for node in range(1, n):
                self.logs[k][node] = self.logs[k-1][self.logs[k-1][node]]
        
        # print([dict(l) for l in self.logs])

    def getKthAncestor(self, node: int, k: int) -> int:
        if node == 0: return -1
        tmp = node, k
        arr = []
        p = 0
        while k:
            if k % 2:
                arr.append((2 ** p, node, self.logs[p][node]))
                node = self.logs[p][node]
            k //= 2
            p += 1
        # print(tmp, arr)
        return node



# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)