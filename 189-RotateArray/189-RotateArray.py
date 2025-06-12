# Last updated: 12/6/2025, 5:52:01 am
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        half = n-k
        for i in range(half//2):
            nums[i], nums[half-i-1] = nums[half-i-1], nums[i]
        for i in range(k//2):
            nums[half+i], nums[n-i-1] = nums[n-i-1], nums[half+i]
        for i in range(n//2):
            nums[i], nums[n-i-1] = nums[n-i-1], nums[i]

        return 0
