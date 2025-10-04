# Last updated: 4/10/2025, 5:17:58 pm
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        best = 0
        l = 0
        r = n-1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            best = max(area, best)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return best