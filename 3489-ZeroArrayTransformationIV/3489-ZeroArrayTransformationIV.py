# Last updated: 20/5/2025, 2:04:04 pm
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        zero = True
        for num in nums:
            if num != 0:
                zero = False
                break
            
        if zero: return 0
    
        n = len(nums)
        def isGood(mid):
            line = [0] * (n + 1)
            for x, y, val in queries[:mid]:
                line[x] += val
                line[y+1] -= val
            s = 0
            for i in range(n):
                s += line[i]
                if nums[i] - s > 0: return False
            
            return True
        
        l = 0
        r = len(queries)

        while l < r:
            mid = (l + r) // 2

            if isGood(mid+1):
                r = mid
            else:
                l = mid + 1
        
        return l+1 if l < len(queries) else -1