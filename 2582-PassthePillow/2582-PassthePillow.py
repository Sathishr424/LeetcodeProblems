# Last updated: 18/11/2025, 2:24:56 am
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # 1, 2, 3, 4, 5 => 17

        m = time // (n - 1)
        rem = time % (n - 1)
        if m % 2:
            return n - rem
        else:
            return rem + 1