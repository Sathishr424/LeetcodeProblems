# Last updated: 12/6/2025, 5:54:36 am
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        diff = min( height[l],  height[r] )
        trap = 0
        while l < r:
            if height[l] < height[r]:
                trap += diff - height[l]
                l += 1
            else:
                trap += diff - height[r]
                r -= 1
            diff = max(diff, min(height[l],  height[r]))

        return trap