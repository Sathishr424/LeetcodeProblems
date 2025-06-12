# Last updated: 12/6/2025, 5:44:30 am
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ret = 0
        n = len(nums)
        left = -1
        zeros = 0

        for i in range(n):
            if nums[i] == 0:
                zeros += 1
                if zeros > k:
                    ret = max(ret, i-(left+1))
                    left += 1
                    while left < n and nums[left] != 0:
                        left += 1
                    zeros -= 1
        
        if zeros <= k:
            ret = max(ret, len(nums)-(left+1))
        
        return ret
        

        