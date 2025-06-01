# Last updated: 1/6/2025, 10:52:41 pm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        l = int(log2(n-1)) + 1
        ret = 0
        
        for bit in range(l):
            cnt = 0
            mask = 1 << bit
            for num in nums:
                cnt += num & mask
            
            for num in range(1, n):
                if cnt == 0: break
                cnt -= num & mask
            
            if cnt: ret += mask
        
        return ret
