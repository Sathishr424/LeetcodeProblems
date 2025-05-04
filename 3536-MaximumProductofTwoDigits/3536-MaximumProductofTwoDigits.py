# Last updated: 4/5/2025, 9:36:16 am
class Solution:
    def maxProduct(self, n: int) -> int:
        n = sorted(list(str(n)))

        return int(n[-1]) * int(n[-2])