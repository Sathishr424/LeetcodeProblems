# Last updated: 14/6/2025, 1:12:16 pm
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        
        n = len(str1)
        m = len(str2)
        
        div = m
        while div:
            if n % div == 0 and m % div == 0:
                st = str2[:div]
                if st * (n // div) == str1 and st * (m // div) == str2: return st
            div -= 1

        return ''