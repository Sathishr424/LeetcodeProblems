# Last updated: 20/9/2025, 7:21:01 pm
class Union:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [0] * n
        self.max_sum = 0

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
        self.max_sum = max(self.max_sum, self.sizes[x])
        self.parents[y] = x
        
        return False

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)

        un = Union(n)

        ret = [0] * n
        for i in range(n-1, -1, -1):
            ret[i] = un.max_sum
            index = removeQueries[i]
            un.sizes[index] = nums[index]
            un.max_sum = max(un.max_sum, nums[index])

            if index + 1 < n and un.sizes[index + 1] > 0:
                un.union(index, index + 1)
            
            if index - 1 >= 0 and un.sizes[index - 1] > 0:
                un.union(index, index - 1)
        
        return ret