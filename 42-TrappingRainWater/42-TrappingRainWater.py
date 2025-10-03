# Last updated: 3/10/2025, 7:54:43 am
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        stack = []
        area = 0
        for i in range(n):
            prev = i
            curr = 0
            while stack and stack[-1][1] < height[i]:
                index, h = stack.pop()
                dis = prev - index
                curr += (height[i] - h) * dis
                prev = index

            if len(stack) == 0 and prev != i:
                dis = i - prev
                curr -= (height[i] - height[prev]) * dis
                prev = i
            
            area += curr
            stack.append((prev, height[i]))
        
        return area
