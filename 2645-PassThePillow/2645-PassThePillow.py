# Last updated: 12/6/2025, 5:37:24 am
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n: return time+1
        rem = time % (n-1)

        return rem+1 if time // (n-1) % 2 == 0 else n-rem

        