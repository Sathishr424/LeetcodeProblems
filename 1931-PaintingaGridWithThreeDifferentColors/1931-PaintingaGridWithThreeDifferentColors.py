# Last updated: 16/5/2025, 1:39:40 am
mod = 10**9 + 7

class Node:
    def __init__(self):
        self.colors = [None, None, None]

class Trie:
    def __init__(self):
        self.node = Node()
        self.memo = {}
    
    def query(self, node, comb, st):
        key = (node, comb)
        if key in self.memo: return self.memo[key]
        if comb == 1:
            return [st]

        ans = []
        rem = comb % 10

        for color in range(3):
            if color == rem: continue
            if node.colors[color] != None:
                ans += self.query(node.colors[color], comb // 10, st * 10 + color)
        self.memo[key] = ans
        return ans
    
    def insert(self, comb):
        node = self.node

        while comb > 1:
            rem = comb % 10

            if node.colors[rem] == None:
                node.colors[rem] = Node()
            node = node.colors[rem]
            
            comb //= 10
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        if m == 1: return 3 * (2 ** (n-1)) % mod
        if n == 1: return 3 * (2 ** (m-1)) % mod
        trie = Trie()

        @cache
        def dfs(row, comb, prev):
            if row == m:
                curr[comb] = 1
                trie.insert(comb)
                return
            
            for color in range(3):
                if prev == color: continue
                dfs(row+1, comb * 10 + color, color)
        
        counts = defaultdict(int)
        curr = defaultdict(int)
        dfs(0, 1, -1)
        graphs_cache = defaultdict(list)

        for comb in curr:
            new_graphs = trie.query(trie.node, comb, 1)
            graphs_cache[comb] = new_graphs
            counts[comb] = len(new_graphs)

        ret = 0
        for i in range(1, n):
            ret = 0
            new_curr = defaultdict(int)
            for comb in curr:
                ret = (ret + curr[comb] * counts[comb] % mod) % mod
                for c in graphs_cache[comb]:
                    new_curr[c] += curr[comb]
            curr = new_curr
        
        return ret