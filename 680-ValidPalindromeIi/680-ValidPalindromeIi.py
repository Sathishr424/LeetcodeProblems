# Last updated: 12/6/2025, 5:47:43 am
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        if n <= 2: return True

        l = 0
        r = n-1
        def helper(x, y):
            while x <= y:
                if s[x] != s[y]: return False
                x += 1
                y -= 1
            return True

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return helper(l+1, r) or helper(l, r-1)
        
        return True


        
