# Last updated: 9/4/2025, 3:06:14 am
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        ret = 0

        for i in range(n):
            index = i
            while stack and stack[-1][1] > heights[i]:
                index, h = stack.pop()
                ret = max(ret, (i-index) * h)
            
            stack.append((index, heights[i]))
        
        for index, h in stack:
            ret = max(ret, (n-index) * h)
        
        return ret