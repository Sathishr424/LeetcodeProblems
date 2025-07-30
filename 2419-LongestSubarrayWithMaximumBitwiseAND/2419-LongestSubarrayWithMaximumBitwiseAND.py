# Last updated: 30/7/2025, 7:51:16 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        max_num = max(nums)

        k = floor(log2(n)) + 1

        table = [[0] * n for _ in range(k)]

        for i in range(n):
            table[0][i] = nums[i]
        
        for power in range(1, k):
            m = 1 << power
            prev_m = m >> 1

            for i in range(n-m+1):
                table[power][i] = table[power - 1][i] & table[power-1][i+prev_m]
        
        def isGood(dis):
            power = floor(log2(dis))
            m = 1 << power
            for i in range(n-dis+1):
                if table[power][i] & table[power][(i + dis) - m] == max_num: return True
            return False

        l = 1
        r = n

        while l < r:
            mid = (l + r + 1) // 2

            if isGood(mid):
                l = mid
            else:
                r = mid - 1

        return l