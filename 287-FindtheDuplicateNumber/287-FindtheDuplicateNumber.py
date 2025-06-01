# Last updated: 1/6/2025, 10:51:44 pm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        l = int(log2(n-1)) + 1
        ret = 0
        
        for bit in range(l+1):
            cnt = 0
            for num in nums:
                cnt += num & (1 << bit)
            
            for num in range(1, n):
                if cnt == 0: break
                cnt -= num & (1 << bit)
            
            if cnt: ret += 1 << bit
        
        return ret
