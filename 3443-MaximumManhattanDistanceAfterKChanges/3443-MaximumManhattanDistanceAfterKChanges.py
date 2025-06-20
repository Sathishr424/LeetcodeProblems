# Last updated: 20/6/2025, 9:23:27 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def helper(h, v, k):
            ans = 0
            x = 0
            y = 0
            for char in s:
                if char in 'WE':
                    if k > 0 and char != h:
                        char = h
                        k -= 1
                    x += 1 if char == 'E' else -1
                elif char in 'SN':
                    if k > 0 and char != v:
                        char = v
                        k -= 1
                    y += 1 if char == 'N' else -1
                ans = cmax(ans, abs(x) + abs(y))
            return ans
        
        ret = helper('W', 'N', k)
        ret = cmax(ret, helper('W', 'S', k))
        ret = cmax(ret, helper('E', 'N', k))
        return cmax(ret, helper('E', 'S', k))