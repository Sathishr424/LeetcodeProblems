# Last updated: 12/6/2025, 5:34:47 am
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def get(x, y):
            res = 0
            a = 1
            prev = x
            ans = 0

            while a <= x:
                res += 1
                a *= 4

            while a <= y:
                ans += (a-prev) * res
                prev = a
                res += 1
                a *= 4
            
            a = max(a//4, x)
            ans += (y - a + 1) * res
            return ans
        
        ret = 0
        for i, j in queries:
            ret += (get(i, j)+1) // 2

        return ret
