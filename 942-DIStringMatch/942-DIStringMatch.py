# Last updated: 10/8/2025, 2:26:11 pm
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if int(s) > finish: return 0
        
        start = str(start - 1)
        finish = str(finish)

        s_n = len(start)
        f_n = len(finish)

        l = len(s)
    
        @cache
        def rec_all(rem):
            if rem == 0: return 1
            ans = 1

            for i in range(limit + 1):
                ans += rec_all(rem - 1)
            return ans
        
        @cache
        def rec(rem):
            if rem == 0: return 1
            ans = 0

            for i in range(limit + 1):
                ans += rec(rem - 1)
            return ans

        def helper(end, m):
            if m == 0 and int(end) >= int(s): return 1
            if m <= 0: return 0
            end_int = int(end)
            @cache
            def rec_strict(index, strict):
                if index == m: 
                    return 1
                
                ans = 0
                if strict:
                    for i in range(min(limit, int(end[index])) + 1):
                        if i == int(end[index]):
                            curr = int(end[:index] + str(i) + '0' * (m - index - 1) + s)
                            if curr <= end_int:
                                ans += rec_strict( index + 1, True )
                        else:
                            ans += rec_strict( index + 1, False )
                else:
                    for i in range(limit + 1):
                        ans += rec_strict( index + 1, False )
                return ans

            ans = 1
            if m >= 2:
                for i in range(1, limit + 1):
                    ans += rec_all(m - 2)

            if m >= 1:
                for i in range(1, min(int(end[0]), limit + 1)):
                    ans += rec(m - 1)

            curr = int(end[0] + '0' * (m - 1) + s)
            if int(end[0]) <= limit and curr <= end_int:
                ans += rec_strict(1, True)

            rec_strict.cache_clear()
            return ans

        ans = helper(finish, f_n - l) - helper(start, s_n - l)
        
        rec_all.cache_clear()
        rec.cache_clear()
        
        return ans
