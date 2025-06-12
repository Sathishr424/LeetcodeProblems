# Last updated: 12/6/2025, 5:54:50 am
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        j = n-1

        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
                n -= 1
            else:
                i += 1
        return n