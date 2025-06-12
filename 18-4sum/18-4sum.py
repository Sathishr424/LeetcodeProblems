# Last updated: 12/6/2025, 5:55:09 am
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        ret = []

        compression = {}
        index = 0
        for num in nums:
            if num not in compression:
                compression[num] = index
                index += 1

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]: continue
                s = target - (nums[i]+nums[j])
                sums = {}
                masks = {}
                for k in range(j+1, n):
                    diff = s-nums[k]
                    if diff in sums:
                        mask = hash((diff, nums[k]))
                        if mask not in masks:
                            ret.append([nums[i], nums[j], diff, nums[k]])
                            masks[mask] = 1
                    
                    sums[nums[k]] = 1
        
        return ret


