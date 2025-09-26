# Last updated: 27/9/2025, 2:51:12 am
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        st = [int(a) for a in str(n)]
        m = len(st)

        @cache
        def rec(index, strict, curr, spec):
            if ((spec and index == m) or index > m) and curr <= target:
                return 1, 0
            if curr > target: return 1, inf
            min_ans = inf
            min_d = 1
            if strict:
                for i in range(st[index], 10):
                    d, ans = rec(index + 1, i == st[index], curr + i, spec)
                    ans = i * d + ans
                    if ans < min_ans:
                        min_d = d
                        min_ans = ans
            else:
                for i in range(10):
                    d, ans = rec(index + 1, False, curr + i, spec)
                    ans = i * d + ans
                    if ans < min_ans:
                        min_d = d
                        min_ans = ans

            return min_d * 10, min_ans

        min_ans = inf
        for i in range(1, 10):
            d, ans = rec(1, i == st[0], i, i >= st[0])
            ans = i * d + ans
            if ans < min_ans:
                min_ans = ans
            d, ans = rec(1, False, i, False)
            ans = i * d + ans
            if ans < min_ans:
                min_ans = ans

        rec.cache_clear()
        return min_ans - n