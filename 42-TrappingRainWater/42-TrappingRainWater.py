# Last updated: 3/10/2025, 8:04:13 am
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = [0] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i - 1])

        right = [0] * n
        for i in range(n-2, -1, -1):
            right[i] = max(right[i + 1], height[i + 1])
        
        area = 0
        for i in range(n):
            max_level = max(min(left[i], right[i]), height[i])
            area += max_level - height[i]
        
        return area