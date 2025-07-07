# Last updated: 7/7/2025, 7:34:58 pm
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)

        @cache
        def rec(index, rem):
            if rem == 0: return 0
            if index == n: return 0
            x, y, val = events[index]

            left = bisect_left(events, [y + 1, 0, 0])
            right = bisect_right(events, [y + 1, 0, 0])

            # print((x, y, val), left, right)

            ans = max(rec(right, rem - 1) + val, rec(index + 1, rem))
            for i in range(left, right):
                ans = max(ans, rec(i, rem))
            return ans
        
        return rec(0, k)