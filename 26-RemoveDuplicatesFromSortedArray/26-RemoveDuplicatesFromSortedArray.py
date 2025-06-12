# Last updated: 12/6/2025, 5:54:53 am
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        prev = 0
        index = 1

        while i < n:
            while i < n and nums[i] == nums[prev]:
                i += 1
            if i >= n: return index
            nums[index], nums[i] = nums[i], nums[index]
            prev = index
            i += 1
            index += 1

        return index