# Last updated: 17/8/2025, 6:30:57 pm
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # 0 0 0 0 1 1 1 1 0 0 1 1 0 0 1 1 0 0 0 0 1 1 0 1
        n = len(nums)

        need = nums.count(1)

        one = 0
        for i in range(need):
            one += nums[i] == 1
        
        ret = need - one

        for i in range(need, n + n - 1):
            one -= nums[(i - need) % n] == 1
            one += nums[i % n] == 1

            ret = min(ret, need - one)
        
        return ret
            
                