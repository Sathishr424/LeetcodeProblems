# Last updated: 1/6/2025, 10:47:47 pm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        l = int(log2(n-1)) + 1
        ret = 0
        
        for bit in range(l+1):
            cnt = 0
            for num in nums:
                if num & (1 << bit):
                    cnt += 1
            
            for num in range(1, n):
                if num & (1 << bit):
                    cnt -= 1
            
            if cnt > 0:
                ret += 2 ** bit
        
        return ret
