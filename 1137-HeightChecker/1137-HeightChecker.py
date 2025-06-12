# Last updated: 12/6/2025, 5:43:56 am
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ret = 0
        for i, height in enumerate(sorted(heights)):
            if height != heights[i]: ret += 1
        
        return ret