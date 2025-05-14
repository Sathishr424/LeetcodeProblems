# Last updated: 14/5/2025, 2:16:32 pm
N = 16
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        self.logs = [[-1] * n for _ in range(N)]

        for i in range(n):
            self.logs[0][i] = parent[i]
        
        for i in range(1, N):
            for j in range(n):
                if self.logs[i-1][j] == -1: continue
                self.logs[i][j] = self.logs[i-1][self.logs[i-1][j]]
    
    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(N-1, -1, -1):
            if (1 << i) <= k:
                if self.logs[i][node] == -1: return -1
                k -= (1 << i)
                node = self.logs[i][node]
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)