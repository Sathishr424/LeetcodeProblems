# Last updated: 12/6/2025, 5:44:39 am
alp = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

class Union:
    def __init__(self, n):
        self.parents = []
        self.size = []
        for i in range(n):
            self.parents.append(i)
            self.size.append(0)
        
    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2: return 0

        if self.size[root1] < self.size[root2]:
            root2, root1 = root1, root2
        
        self.size[root1] += self.size[root2]
        self.parents[root2] = root1
        return 1

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        uf = Union(26)
        left = 0
        right = n-1
        while left <= right:
            if equations[left][1] == '!':
                equations[left], equations[right] = equations[right], equations[left]
                right -= 1
            else:
                uf.union(alp[equations[left][0]], alp[equations[left][-1]])
                left += 1

        for i in range(left, n):
            if uf.find(alp[equations[i][0]]) == uf.find(alp[equations[i][-1]]): return False
        return True
