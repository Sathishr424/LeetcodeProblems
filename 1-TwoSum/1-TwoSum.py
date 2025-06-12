# Last updated: 12/6/2025, 5:55:49 am
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            if nums[i] in hash: return [i, hash[nums[i]]]
            else:
                hash[target-nums[i]] = i
        return []