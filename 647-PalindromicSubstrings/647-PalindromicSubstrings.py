# Last updated: 12/6/2025, 5:47:56 am
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ret = n
        first = []
        second = []

        for i in range(n-1):
            if s[i] == s[i+1]:
                second.append(1)
                ret += 1
            else:
                second.append(0)
            first.append(1)
        
        for i in range(2, n):
            for j in range(n-i):
                if first[j+1] and s[j] == s[j+i]:
                    first[j] = 1
                    ret += 1
                else:
                    first[j] = 0
            first, second = second, first

        return ret