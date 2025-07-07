# Last updated: 7/7/2025, 7:46:07 pm
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)

        @cache
        def rec(index, rem):
            if rem == 0: return 0
            if index == n: return 0
            x, y, val = events[index]

            next_index = bisect_left(events, [y + 1, 0, 0])

            ans = max(rec(next_index, rem - 1) + val, rec(index + 1, rem))
            return ans
        
        ans = rec(0, k)
        rec.cache_clear()
        return ans