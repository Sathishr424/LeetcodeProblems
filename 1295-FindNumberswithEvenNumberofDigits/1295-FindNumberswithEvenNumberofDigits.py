# Last updated: 30/4/2025, 7:51:28 am
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