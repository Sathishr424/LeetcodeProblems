# Last updated: 12/6/2025, 5:55:24 am
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ans = 0
        while l < r:
            ans = max(ans, (r-l) * min(height[l], height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ans