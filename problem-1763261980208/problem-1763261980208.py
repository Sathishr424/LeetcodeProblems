# Last updated: 16/11/2025, 8:29:40 am
class Solution:
    def countDistinct(self, n: int) -> int:
        arr = [int(d) for d in str(n)]
        m = len(arr)

        @cache
        def rec(index, prev, strict):
            if index == m:
                return 1
            ans = 0

            if strict:
                for i in range(1, arr[index] + 1):
                    ans += rec(index + 1, i, i == arr[index])
            else:
                for i in range(1, 10):
                    ans += rec(index + 1, i, False)
                

            return ans
        
        @cache
        def rec2(index, prev):
            if index == m - 1:
                return 1
            
            ans = 1
            
            for i in range(1, 10):
                ans += rec2(index + 1, i)

            return ans

        ans = 0
        for i in range(1, arr[0] + 1):
            ans += rec(1, i, i == arr[0])
        rec.cache_clear()

        if m > 1:
            for i in range(1, 10):
                ans += rec2(1, i)
        
        rec2.cache_clear()
        return ans

# 1000000000000000