# Last updated: 12/6/2025, 5:42:01 am
class Solution:
    def generateTheString(self, n: int) -> str:
        if n==1: return 'a'
        if n%2 == 0: return 'a'*(n-1) + 'b'
        else: return 'a'*(n-2) + 'bc'