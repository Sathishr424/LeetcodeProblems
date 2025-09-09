# Last updated: 9/9/2025, 9:45:04 pm
class Node:
    def __init__(self):
        self.childs = {}

class Trie:
    def __init__(self):
        self.node = Node()

    def insert(self, word):
        node = self.node

        for char in word:
            if char not in node.childs:
                node.childs[char] = Node()
            node = node.childs[char]

    def get(self, word, node, s=''):
        # print(word, list(node.childs.keys()))
        ans = 0
        for char in node.childs:
            if char not in word:
                ans = max(ans, self.get(word, node.childs[char], s + char) + 1)
        # print(word, s, ans)
        return ans
    
class Solution:
    def longestPath(self, parent: List[int], relation: str) -> int:
        n = len(parent)
        graph = defaultdict(list)
        edges = []

        for i in range(1, n):
            par = parent[i]
            graph[par].append(i)
            graph[i].append(par)
        
        max_ans = 1
        
        def dfs(x, par, prev, curr):
            nonlocal max_ans
            ans = curr
            arr = []
            for y in graph[x]:
                if y == par: continue
                new_curr = dfs(y, x, relation[y], 1)
                if relation[y] != prev:
                    arr.append(new_curr)
                    ans = max(ans, new_curr + curr)
            
            arr.sort()
            max_ans = max(max_ans, sum(arr[-2:]) + 1)

            return ans
        
        dfs(0, -1, relation[0], 1)
        return max_ans