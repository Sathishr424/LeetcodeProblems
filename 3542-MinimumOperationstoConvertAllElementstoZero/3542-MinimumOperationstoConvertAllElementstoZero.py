# Last updated: 10/11/2025, 3:57:06 pm
from math import floor, log2

class sparseTable:
    def __init__(self, nums):
        self.nums = nums
        n = len(nums)
        self.n = n
        k_log = floor(log2(n)) + 1
                
        self.logs = [[0] * n for _ in range(k_log)]

        for i in range(n):
            self.logs[0][i] = nums[i]

        for power in range(1, k_log):
            m = 1 << power
            prev_m = m >> 1

            for i in range(n-m+1):
                self.logs[power][i] = min(self.logs[power - 1][i], self.logs[power - 1][i + prev_m])
    
    def query(self, l, r):
        dis = r - l + 1
        power = floor(log2(dis))
        return min(self.logs[power][l], self.logs[power][r - (1 << power) + 1])

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        indexes = defaultdict(list)
        for i, num in enumerate(nums):
            indexes[num].append(i)
        
        table = sparseTable(nums)
        op = 0
        for num in indexes.keys():
            if num == 0: continue
            prev = indexes[num][0]
            for index in indexes[num]:
                min_num = table.query(prev, index)
                if min_num < num:
                    op += 1
                    prev = index
            op += 1
        
        return op
