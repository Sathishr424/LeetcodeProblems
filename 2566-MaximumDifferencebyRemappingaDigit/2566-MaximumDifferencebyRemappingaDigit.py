# Last updated: 14/6/2025, 1:21:00 pm
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        
        div = min(n, m)
        while div:
            if n % div == 0 and m % div == 0:
                st = str2[:div]
                if st * (n // div) == str1 and st * (m // div) == str2: return st
            div -= 1

        return ''