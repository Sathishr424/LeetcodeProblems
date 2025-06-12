# Last updated: 12/6/2025, 5:49:12 am
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(1,(n//2)+1):
            if n % i != 0: continue
            j = i
            tmp = s[:i]
            while j <= (n-i):
                if s[j:j+i] != tmp: break
                j += i
            if j == n: return True
        return False

