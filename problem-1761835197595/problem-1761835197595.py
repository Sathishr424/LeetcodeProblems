# Last updated: 30/10/2025, 8:09:57 pm
class Solution:
    def minMaxDifference(self, num: int) -> int:
        mn = num
        mx = num

        def swap(i, j, x):
            d = 1
            res = 0
            while x:
                rem = x % 10
                if rem == i:
                    rem = j
                res = rem * d + res
                d *= 10
                x //= 10

            return res
        
        for i in range(10):
            for j in range(10):
                if i == j: continue
                val = swap(i, j, num)
                mn = min(mn, val)
                mx = max(mx, val)

        return mx - mn