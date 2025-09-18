# Last updated: 18/9/2025, 4:56:43 pm
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
        
        # print(left)
        # print(right)

        length = [0] * n
        arr = []
        for i in range(n):
            length[i] = (i - left[i] + 1) + (right[i] - i)
            arr.append((nums[i], (i - left[i] + 1) + (right[i] - i)))
        
        # print(length)

        arr.sort(key=lambda x: (x[0], -x[1]))
        # print(arr)

        prefix = [0] * (n + 1)
        maxi = 0
        for i in range(n-1, -1, -1):
            maxi = max(arr[i][1], maxi)
            prefix[i] = maxi
        
        # print([a for a, _ in arr])
        # print(prefix)

        for window in range(1, n + 1):
            maxi = threshold / window

            index = bisect_right(arr, (maxi, inf))
            # print(window, maxi, index)

            if prefix[index] >= window:
                return window
        
        return -1