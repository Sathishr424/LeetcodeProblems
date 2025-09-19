# Last updated: 20/9/2025, 2:29:00 am
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = [int(num) for num in str(n)]
        m = len(s) - 1

        @cache
        def rec(index, mask, strict):
            # print(index, format(mask, '10b'), strict)
            if index == len(s):
                return 1
            ans = 0
            for d in range(10):
                if strict:
                    if d <= s[index] and mask & (1 << d) == 0:
                        ans += rec(index + 1, mask | (1 << d), d == s[index])
                elif mask & (1 << d) == 0:
                    ans += rec(index + 1, mask | (1 << d), False)
            return ans
        
        @cache
        def rec2(index, mask):
            if index == m: return 1
            ans = 1
            for d in range(10):
                if mask & (1 << d) == 0:
                    ans += rec2(index + 1, mask | (1 << d))
            return ans

        ans = 0
        for i in range(1, s[0] + 1):
            ans += rec(1, 1 << i, i == s[0])

        if m > 0:
            for i in range(1, 10):
                curr = rec2(1, 1 << i)
                ans += curr
        rec.cache_clear()
        rec2.cache_clear()
        time.sleep(0.05)
        return ans