# Last updated: 10/8/2025, 12:30:40 pm
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
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        sorted = []
        indexes = [-1] * n
        for i in range(n):
            indexes[nums[i]] = i
            sorted.append((nums[i], i))
        
        sorted.sort()
        for i in range(n):
            if sorted[i][1] != i: break
        else:
            return 0

        prev = -1
        for i in range(n):
            if sorted[i][1] != i:
                if prev == -1:
                    prev = sorted[i][0]
                else:
                    prev &= sorted[i][0]
        
        if prev == 0: return 0
        index = indexes[prev]
        un = Union(n)
        for i, num in enumerate(nums):
            if num & prev == prev:
                un.union(i, index)
        
        # print(un.parents)
        for i in range(n):
            if un.find(sorted[i][1]) != un.find(i): return 0
        
        return nums[index]

        