# Last updated: 22/7/2025, 12:30:17 am
alp = 'abcdefghijklmnopqrstuvwxyz'
ALP = alp.upper()
dig = '01234567890'
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        @cache
        def rec(index, lower, upper, digit, prev, prev_prev, cnt):
            if cnt > 20: return inf
            if index >= n:
                if not lower:
                    return rec(index, True, upper, digit, '-', '-', cnt + 1) + 1
                if not upper:
                    return rec(index, lower, True, digit, '-', '-', cnt + 1) + 1
                if not digit:
                    return rec(index, lower, upper, True, '-', '-', cnt + 1) + 1
                if cnt < 6:
                    return rec(index, lower, upper, digit, '-', '-', cnt + 1) + 1
                if lower and upper and digit: return 0
                return inf
            
            ans = inf
            curr = password[index]

            p_digit = digit
            p_lower = lower
            p_upper = upper
            
            digit = digit or curr in dig
            lower = lower or curr in alp
            upper = upper or curr in ALP

            if prev != '-' and password[index] == prev and password[index] == prev_prev:
                ans = min(ans, rec(index + 1, p_lower, p_upper, p_digit, prev, prev_prev, cnt) + 1) # delete
                if not digit:
                    ans = min(ans, rec(index, lower, upper, True, '-', prev, cnt + 1) + 1)
                    ans = min(ans, rec(index + 1, lower, upper, True, '-', prev, cnt + 1) + 1)
                if not lower:
                    ans = min(ans, rec(index, True, upper, digit, '-', prev, cnt + 1) + 1)
                    ans = min(ans, rec(index + 1, True, upper, digit, '-', prev, cnt + 1) + 1)
                if not upper:
                    ans = min(ans, rec(index, lower, True, digit, '-', prev, cnt + 1) + 1)
                    ans = min(ans, rec(index + 1, lower, True, digit, '-', prev, cnt + 1) + 1)
                if digit and upper and lower:
                    ans = min(ans, rec(index, lower, upper, digit, '-', prev, cnt + 1) + 1)
                    ans = min(ans, rec(index + 1, lower, upper, digit, '-', prev, cnt + 1) + 1)
            else:
                ans = min(ans, rec(index + 1, lower, upper, digit, curr, prev, cnt + 1))
                ans = min(ans, rec(index + 1, p_lower, p_upper, p_digit, prev, prev_prev, cnt) + 1) # delete
                if not digit:
                    ans = min(ans, rec(index + 1, lower, upper, True, '-', prev, cnt + 1) + 1) # replace
                    ans = min(ans, rec(index, lower, upper, True, '-', curr, cnt + 1) + 1) # insert
                if not lower:
                    ans = min(ans, rec(index + 1, True, upper, digit, '-', prev, cnt + 1) + 1) # replace
                    ans = min(ans, rec(index, True, upper, digit, '-', curr, cnt + 1) + 1) # insert
                if not upper:
                    ans = min(ans, rec(index + 1, lower, True, digit, '-', prev, cnt + 1) + 1) # replace
                    ans = min(ans, rec(index, lower, True, digit, '-', curr, cnt + 1) + 1) # insert

            return ans
        
        ans = rec(0, False, False, False, '-', '-', 0)
        rec.cache_clear()
        return ans