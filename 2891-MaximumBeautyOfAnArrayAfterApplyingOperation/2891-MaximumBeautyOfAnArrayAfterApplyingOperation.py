# Last updated: 12/6/2025, 5:36:38 am
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        cnt = 1
        ret = 1
        prev = 0
        for i in range(1, n):
            if nums[prev]+k >= nums[i]-k:
                cnt += 1
                ret = max(ret, cnt)
            else:
                prev += 1
                while prev < i and nums[prev]+k < nums[i]-k:
                    prev += 1
                    cnt -= 1
        return ret