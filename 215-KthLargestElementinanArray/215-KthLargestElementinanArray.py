# Last updated: 9/10/2025, 11:27:05 am
# Same solution as above except that the partition ordering is reversed
# and doesn't use recursion.
# O(1) space.
class Solution:
    def partition(self, nums, left, right):
        pivot = nums[right]

        '''
        nums[left:i] contains elements >= pivot
        nums[i:right] contains element less than the pivot.
        '''
        i = left
        for j in range(left, right):
            if (nums[j] > pivot) or (nums[j] == pivot and (j % 2 == 0)):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i
    
    def quick_select(self, nums, left, right, target):
        while left <= right:
            p = self.partition(nums, left, right)
            if p == target:
                return p
            elif p < target:
                left = p + 1
            else:
                right = p - 1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nums[self.quick_select(nums, 0, len(nums) - 1, k - 1)]