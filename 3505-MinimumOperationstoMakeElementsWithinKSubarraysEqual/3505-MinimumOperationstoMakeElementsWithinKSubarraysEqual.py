# Last updated: 28/6/2025, 6:36:30 pm
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        left = n
        for i, num in enumerate(nums):
            if num >= k:
                left = i
                break
        
        mid = n // 2
        # if left == mid and nums[left] == k: return 0
        # if n % 2 == 0 and left == mid - 1 and nums[left + 1] == k: return 0

        # [1, 2, 3, 5, _7_, 8]
        # [1, _2_, 3, 5, 7, 8]

        # [1, 2, 3, 5, _7_, 8, 9]
        # [1, _2_, 3, 5, 7, 8, 9]

        ret = 0
        if left <= mid:
            for i in range(left, mid + 1):
                ret += nums[i] - k
                nums[i] = k
        elif left > mid:
            for i in range(mid, left):
                ret += k - nums[i]
                nums[i] = k
        # print(nums)
        return ret


