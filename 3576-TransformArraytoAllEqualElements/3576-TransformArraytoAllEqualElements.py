# Last updated: 9/6/2025, 1:54:22 am
class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        def check(m):
            new_nums = nums + []
            op = k
            for i in range(n-1):
                if new_nums[i] != m:
                    new_nums[i] *= -1
                    new_nums[i+1] *= -1
                    op -= 1
            return new_nums[-1] == m and op >= 0
        
        return check(-1) or check(1)
            
