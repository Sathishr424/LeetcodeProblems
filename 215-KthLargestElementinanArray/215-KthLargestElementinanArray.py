# Last updated: 9/10/2025, 10:55:34 am
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

        [3, 2, 1, 5, 6, 4]

        while l < r:
            mid = (l + r + 1) // 2

            large = 0
            equal = 0
            for i in range(n):
                if nums[i] > mid:
                    large += 1
                elif nums[i] == mid:
                    equal += 1
            # print((l, mid, r), large, equal, k - large)
            if k - large <= equal:
                l = mid
            else:
                r = mid - 1
        
        # print(l)
        return l
                