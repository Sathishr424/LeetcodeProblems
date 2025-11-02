# Last updated: 2/11/2025, 7:58:45 am
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        self.k = floor(log2(n)) + 1

        self.logs = [[-1] * n for _ in range(self.k)]

        for i in range(n):
            self.logs[0][i] = parent[i]
        
        for i in range(1, self.k):
            for j in range(n):
                if self.logs[i - 1][j] == -1: continue
                self.logs[i][j] = self.logs[i-1][ self.logs[i - 1][j] ]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(31, -1, -1):
            if (1 << i) <= k:
                node = self.logs[i][node]
                if node == -1: return -1
                k -= (1 << i)
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)