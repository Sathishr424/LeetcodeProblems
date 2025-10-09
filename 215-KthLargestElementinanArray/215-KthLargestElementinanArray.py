# Last updated: 9/10/2025, 11:27:35 am
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        small = nums[0]
        large = nums[0]

        for num in nums:
            if num < small:
                small = num
            elif num > large:
                large = num
        
        l = small
        r = large
        
        while l < r:
            mid = (l + r + 1) // 2

            large = 0
            equal = 0
            for i in range(n):
                if nums[i] > mid:
                    large += 1
                elif nums[i] == mid:
                    equal += 1

            if k - large <= equal:
                l = mid
            else:
                r = mid - 1
        
        return l
                