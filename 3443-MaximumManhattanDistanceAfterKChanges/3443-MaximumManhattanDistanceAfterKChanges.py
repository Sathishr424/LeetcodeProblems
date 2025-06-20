# Last updated: 20/6/2025, 8:23:12 pm
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        ret = 0

        def helper(h, v, k):
            ans = 0
            x = 0
            y = 0
            for char in s:
                if char in 'WE':
                    if k > 0 and char != h:
                        x += 1 if h == 'E' else -1
                        k -= 1
                    else:
                        x += 1 if char == 'E' else -1
                elif char in 'SN':
                    if k > 0 and char != v:
                        y += 1 if v == 'N' else -1
                        k -= 1
                    else:
                        y += 1 if char == 'N' else -1
                ans = max(ans, abs(x) + abs(y))
            return ans
        
        ret = max(ret, helper('W', 'N', k))
        ret = max(ret, helper('W', 'S', k))
        ret = max(ret, helper('E', 'N', k))
        ret = max(ret, helper('E', 'S', k))
        return ret