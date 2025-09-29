# Last updated: 29/9/2025, 4:09:56 pm
class Union:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y: return True

        if self.sizes[y] > self.sizes[x]:
            x, y = y, x

        self.sizes[x] += self.sizes[y]
        self.parents[y] = x
        
        return False

class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)

        un = Union(n)
        for i, j in swaps:
            un.union(i, j)

        parents = [[] for _ in range(n)]
        for i in range(n):
            par = un.find(i)
            parents[par].append((nums[i], i))

        for i in range(n):
            parents[i].sort()

        s = 0
        for i in range(0, n, 2):
            par = un.find(i)
            num, index = parents[par].pop()
            s += num

        for i in range(1, n, 2):
            s -= parents[un.find(i)].pop()[0]

        return s

        