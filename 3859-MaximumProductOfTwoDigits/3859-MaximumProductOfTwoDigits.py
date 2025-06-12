# Last updated: 12/6/2025, 5:33:24 am
class Solution:
    def maxProduct(self, n: int) -> int:
        n = sorted(list(str(n)))

        return int(n[-1]) * int(n[-2])