# Last updated: 21/8/2025, 5:14:28 pm
cmax = lambda x, y: x if x > y else y

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_rect = 0
        stack = []
        for i in range(n):
            left = i
            while stack and stack[-1][0] > heights[i]:
                height, left = stack.pop()
                max_rect = cmax(max_rect, height * (i - left))
            stack.append((heights[i], left))

        while stack:
            height, left = stack.pop()
            max_rect = cmax(max_rect, height * (n - left))

        return max_rect