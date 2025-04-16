# Last updated: 17/4/2025, 12:48:15 am
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        ret = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]: continue
                s = target - (nums[i]+nums[j])
                sums = {}
                masks = {}
                for k in range(j+1, n):
                    if nums[k] in masks: continue
                    diff = s-nums[k]
                    if diff in sums:
                        ret.append([nums[i], nums[j], diff, nums[k]])
                        masks[nums[k]] = 1
                    
                    sums[nums[k]] = 1
        
        return ret


