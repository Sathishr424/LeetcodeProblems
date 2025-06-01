# Last updated: 2/6/2025, 2:38:07 am
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow