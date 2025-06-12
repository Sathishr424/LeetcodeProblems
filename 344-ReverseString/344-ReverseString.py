# Last updated: 12/6/2025, 5:50:19 am
class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n//2):
            s[i], s[n-(i+1)] = s[n-(i+1)], s[i]
        