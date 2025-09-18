# Last updated: 18/9/2025, 5:01:47 pm
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

        max_window = 0
        for i in range(n-1, -1, -1):
            max_window = max(arr[i][1], max_window)

            if arr[i][0] > threshold / max_window:
                return max_window
        
        return -1