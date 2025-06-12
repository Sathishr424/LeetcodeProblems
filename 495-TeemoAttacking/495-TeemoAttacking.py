# Last updated: 12/6/2025, 5:48:57 am
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        prev = -1
        for t in timeSeries:
            if t <= prev:
                ans -= (prev - t)+1
            prev = t+duration-1
            ans += duration
        return ans