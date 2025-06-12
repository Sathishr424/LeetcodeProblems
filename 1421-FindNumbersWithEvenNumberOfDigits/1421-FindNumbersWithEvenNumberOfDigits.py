# Last updated: 12/6/2025, 5:42:30 am
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            cnt = 0
            while num:
                num //= 10
                cnt += 1
            
            ret += cnt % 2 == 0
        
        return ret