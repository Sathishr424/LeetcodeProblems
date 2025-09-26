# Last updated: 26/9/2025, 2:05:33 pm
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        nums.sort()
        for i in range(n):
            for j in range(i+1, n):
                a = nums[i]
                b = nums[j]

                left = abs(a - b) + 1
                right = a + b - 1

                if left <= right:
                    l = bisect_left(nums, left, lo=j+1)
                    r = bisect_right(nums, right, lo=j+1)
                    cnt += r - l

        return cnt