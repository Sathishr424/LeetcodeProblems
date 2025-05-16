# Last updated: 16/5/2025, 11:01:06 pm
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # abasdsadsdcsacdeeeff a.*cdeeeff
        m = len(s)
        n = len(p)

        @cache
        def rec(left, right):
            if right == n: return left == m
            elif right+1 < n and p[right+1] == '*' and rec(left, right+1): return True
            elif left == m: return p[right] == '*' and rec(left, right+1)
            
            if s[left] == p[right]:
                return rec(left+1, right+1)
            elif p[right] == '.':
                return rec(left+1, right+1)
            elif p[right] == '*':
                if rec(left, right+1): return True
                elif p[right-1] == '.' or p[right-1] == s[left]:
                    return rec(left+1, right)

            return False

        return rec(0, 0)