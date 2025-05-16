# Last updated: 16/5/2025, 10:40:47 pm
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # abasdsadsdcsacdeeeff a.*cdeeeff
        m = len(s)
        n = len(p)
        @cache
        def rec(left, right):
            if left == m and right == n: return True
            if left < m and right < n:
                if s[left] == p[right]:
                    if right+1 < n and p[right+1] == '*' and rec(left, right+1): return True
                    return rec(left+1, right+1)
                elif p[right] == '.':
                    if right+1 < n and p[right+1] == '*' and rec(left, right+1): return True
                    return rec(left+1, right+1)
                elif p[right] == '*':
                    prev = right-1
                    if rec(left, right+1): return True
                    if prev >= 0 and (p[prev] == '.' or p[prev] == s[left]):
                        return rec(left+1, right+1) or rec(left+1, right)
                elif right+1 < n and p[right+1] == '*':
                    return rec(left, right+2)
            elif right < n:
                if p[right] == '*': return rec(left, right+1)
                elif right+1 < n and p[right+1] == '*': return rec(left, right+2)
            return False

        return rec(0, 0)