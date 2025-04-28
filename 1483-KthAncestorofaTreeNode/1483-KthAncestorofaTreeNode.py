# Last updated: 28/4/2025, 6:55:31 pm
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        m = len(bin(n)) - 2
        self.logs = [[-1] * n for _ in range(m)]

        for node in range(1, n):
            self.logs[0][node] = parent[node]

        for k in range(1, m):
            for node in range(1, n):
                if self.logs[k-1][node] == -1: continue
                self.logs[k][node] = self.logs[k-1][self.logs[k-1][node]]

    def getKthAncestor(self, node: int, k: int) -> int:
        p = 0
        while k:
            if k % 2:
                node = self.logs[p][node]
                if node == -1: return -1
            k //= 2
            p += 1
        
        return node



# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)