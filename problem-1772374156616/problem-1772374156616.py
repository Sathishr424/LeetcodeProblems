# Last updated: 3/1/2026, 7:39:16 PM
1class Solution:
2    def trimTrailingVowels(self, s: str) -> str:
3        vowels = "aeiou"
4
5        while len(s) and s[-1] in vowels:
6            s = s[:-1]
7
8        return s