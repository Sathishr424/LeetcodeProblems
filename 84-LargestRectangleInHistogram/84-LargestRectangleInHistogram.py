# Last updated: 12/6/2025, 5:53:41 am
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        ret = 0

        for i, h in enumerate(heights):
            index = i
            while stack and stack[-1][1] > h:
                index, prev_h = stack.pop()
                ret = max(ret, (i-index) * prev_h)
            
            stack.append((index, h))
        
        while stack:
            index, h = stack.pop()
            ret = max(ret, (n-index) * h)
        
        return ret