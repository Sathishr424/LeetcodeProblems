# Last updated: 18/9/2025, 4:58:08 pm
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)

        stack = []
        left = [i for i in range(n)]
        right = [i for i in range(n)]
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                left[i] = left[stack.pop()]

            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                right[i] = right[stack.pop()]

            stack.append(i)
        
        arr = []
        for i in range(n):
            arr.append((nums[i], (i - left[i] + 1) + (right[i] - i)))
        arr.sort(key=lambda x: (x[0], -x[1]))

        prefix = [0] * (n + 1)
        maxi = 0
        for i in range(n-1, -1, -1):
            maxi = max(arr[i][1], maxi)
            prefix[i] = maxi

        for window in range(n, 0, -1):
            maxi = threshold / window

            index = bisect_right(arr, (maxi, inf))

            if prefix[index] >= window:
                return window
        
        return -1